from django import forms
from django.forms import Textarea

from CARSBG.services.models import CarService, RentACar


class CreateCarServiceForm(forms.ModelForm):
    class Meta:
        model = CarService
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 10}),
        }


class CreateRentACarForm(forms.ModelForm):
    class Meta:
        model = RentACar
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 10}),
            'cars': Textarea(attrs={'cols': 20, 'rows': 10}),
        }

