from django.core.validators import RegexValidator
from django.db import models
from datetime import date
import math


class PetType(models.Model):
    pet_type = models.CharField(max_length=20)

    def __str__(self):
        return self.pet_type


class Pet(models.Model):
    pet_type = models.ForeignKey(PetType, on_delete=models.DO_NOTHING)
    pet_name = models.CharField(default='', max_length=50)
    birthday = models.DateField(default='',
                                validators=[RegexValidator
                                            (regex='^[1-2]\\d{3}-[0-1]\\d-[0-3]\\d$')])
    pet_passport_number = models.IntegerField(default='',
                                              blank=True, null=True)
    reason = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.pet_name

    @property
    def age(self):
        today = date.today()
        age = math.trunc(today.year - self.birthday.year -
                         ((today.month, today.day) <
                          (self.birthday.month, self.birthday.day)))
        return age

    @property
    def has_passport(self) -> bool:
        return bool(self.pet_passport_number)

    @property
    def high(self):
        high = Measure.objects.filter(pet_id=self.id).latest('measure_date')
        return high.pet_high

    @property
    def weight(self):
        weight = Measure.objects.filter(pet_id=self.id).latest('measure_date')
        return weight.pet_weight

    @property
    def feed_amount(self):
        feed_amount = PetFeed.objects.get(pet_type=self.pet_type)
        return feed_amount.pet_feed_amount
        

class Measure(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    pet_high = models.IntegerField(default='')
    pet_weight = models.IntegerField(default='')
    measure_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pet)


class MedCard(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    pet_sickness = models.CharField(max_length=250)
    MedCard_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.pet)


class PetFeed(models.Model):
    pet_type = models.OneToOneField(PetType, on_delete=models.DO_NOTHING)
    pet_feed_amount = models.IntegerField()
    pet_feed_price = models.FloatField()

    def __str__(self):
        return str(self.pet_type)
