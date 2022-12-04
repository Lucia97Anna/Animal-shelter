import django_filters
from pet.models import PetType, Pet
from django import forms


class PetFilter(django_filters.FilterSet):
    pet_type = django_filters.ModelChoiceFilter(
        queryset=PetType.objects.all(),
        label="Type",
        widget=forms.Select(attrs={'class': 'span6 small-margin-top small-margin-bottom'}))

    class Meta:
        model = Pet
        fields = ['pet_type']
