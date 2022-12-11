from django.shortcuts import render
from django.views import generic

from CARSBG.services.forms import CreateCarServiceForm, CreateRentACarForm


# Create your views here.


def services_types(request):
    return render(request, 'services/main.html')


class CreateCarService(generic.CreateView):
    form_class = CreateCarServiceForm
    template_name = 'services/create-car-service.html'
    success_url = 'index'


class CreateRentACar(generic.CreateView):
    form_class = CreateRentACarForm
    template_name = 'services/create-rent-a-car.html'
    success_url = 'index'

