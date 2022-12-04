from django.shortcuts import render, redirect
from pet.forms import PetForm, MeasureForm
from pet.models import Pet, Measure, MedCard
from pet.filters import PetFilter
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView, CreateView


def pet_and_measure_form(request, pk=0):
    if request.method == 'GET':
        try:
            if pk == 0:
                pet_form = PetForm()
                measure_form = MeasureForm()
            else:
                pet = Pet.objects.get(id=pk)
                pet_form = PetForm(instance=pet)
                pet_measure = Measure.objects.filter(pet_id=pk).latest('measure_date')
                measure_form = MeasureForm(instance=pet_measure)
            context = {'pet_form': pet_form, 'measure_form': measure_form}
        except ObjectDoesNotExist:
            raise Http404
        return render(request, 'pet/add_new_pet.html', context)
    elif request.method == 'POST':
        if pk == 0:
            pet_form = PetForm(request.POST)
            measure_form = MeasureForm(request.POST)
        else:
            pet = Pet.objects.get(id=pk)
            pet_form = PetForm(request.POST, instance=pet)
            pet_measure = Measure.objects.filter(pet_id=pk).latest('measure_date')
            measure_form = MeasureForm(request.POST, instance=pet_measure)
        if pet_form.is_valid() and measure_form.is_valid():
            pet = pet_form.save()
            measure = measure_form.save(False)

            measure.pet = pet
            measure.save()
        return redirect('search')


class PetDeleteView(UpdateView):
    model = Pet
    fields = ['reason']
    template_name = 'pet/delete_pet_form.html'
    success_url = '/'


class PetMeasureView(CreateView):
    model = Measure
    fields = ['pet', 'pet_high', 'pet_weight']
    template_name = 'pet/add_measure.html'
    success_url = '/'


class PetMedCardView(CreateView):
    model = MedCard
    fields = ['pet', 'pet_sickness']
    template_name = 'pet/add_medcard.html'
    success_url = '/'


def med_card_view(request, pk):
    try:
        med_card_model = MedCard.objects.filter(pet_id=pk)
        context = {'med_card_model': med_card_model}
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'pet/medcard_detail.html', context)


def measure_view(request, pk):
    try:
        measure_model = Measure.objects.filter(pet_id=pk)
        context = {'measure_model': measure_model}
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'pet/measure_detail.html', context)


def type_search(request):
    filter = PetFilter(request.GET,
                       queryset=Pet.objects.filter(reason__isnull=True))
    context = {'filter': filter}
    return render(request, 'pet/list_of_pet.html', context=context)
