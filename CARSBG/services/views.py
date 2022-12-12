from django.shortcuts import render
from django.views import generic

from CARSBG.services.forms import CreateCarServiceForm, CreateRentACarForm
from CARSBG.services.models import CarService, RentACar

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


class CarServicesPost(generic.CreateView):
    def get(self, request, *args, **kwargs):
        car_services = CarService.objects.all()

        context = {
            'car_services': car_services
        }

        return render(request, 'services/car-services-posts.html', context)

    def post(self, request, *args, **kwargs):
        pass


class RentACarPosts(generic.CreateView):
    def get(self, request, *args, **kwargs):
        rent_a_cars = RentACar.objects.all()

        context = {
            'rent_a_cars': rent_a_cars
        }

        return render(request, 'services/rent-a-car-posts.html', context)

    def post(self, request, *args, **kwargs):
        pass
