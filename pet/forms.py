from django import forms
from pet.models import Pet, Measure


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_type', 'pet_name', 'birthday', 'pet_passport_number']
        widgets = {
            'birthday': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'})}


class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ['pet_high', 'pet_weight']
