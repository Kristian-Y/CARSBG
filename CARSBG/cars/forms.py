from django import forms
from django.forms import Textarea

from CARSBG.cars.models import Car


class FilterForm(forms.Form):
    OPTIONS = (
        ("BMW", "BMW"),
        ("AUDI", "Audi"),
        ("Mercedes", "Mercedes"),
        ("Honda", "Honda"),
        ("Toyota", "Toyota"),
        ("Skoda", "Skoda"),
        ("VW", "VW"),
        ("Pegeot", "Pegeot"),
        ("Kia", "Kia"),
        ("Suzuki", "Suzuki")
    )
    brand = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS,
    )


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 17, 'rows': 10}),
        }
