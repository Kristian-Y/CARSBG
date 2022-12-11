from django import forms

from CARSBG.services.models import CarService, RentACar


class CreateCarServiceForm(forms.ModelForm):
    class Meta:
        model = CarService
        fields = '__all__'


class CreateRentACarForm(forms.ModelForm):
    class Meta:
        model = RentACar
        fields = '__all__'

