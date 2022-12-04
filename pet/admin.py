from django.contrib import admin

from pet.models import Pet, PetType, Measure, MedCard, PetFeed

admin.site.register(Pet)
admin.site.register(PetType)
admin.site.register(Measure)
admin.site.register(MedCard)
admin.site.register(PetFeed)
