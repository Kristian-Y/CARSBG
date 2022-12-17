from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from CARSBG.services.forms import CreateCarServiceForm, CreateRentACarForm
from CARSBG.services.models import CarService, RentACar


# Create your views here.


def services_types(request):
    return render(request, 'services/main.html')


class CreateCarService(generic.CreateView):
    form_class = CreateCarServiceForm
    template_name = 'services/create-car-service.html'

    def post(self, request, *args, **kwargs):
        create_car_service_form = CreateCarServiceForm(request.POST)
        if create_car_service_form.is_valid():
            car_service = create_car_service_form.save(commit=False)
            car_service.user = request.user
            car_service.save()
            return redirect('car-services-posts')

        context = {
            'form': create_car_service_form
        }
        return render(request, self.template_name, context)


class CreateRentACar(generic.CreateView):
    form_class = CreateRentACarForm
    template_name = 'services/create-rent-a-car.html'
    success_url = 'index'

    def post(self, request, *args, **kwargs):
        create_rent_service_form = CreateRentACarForm(request.POST)
        if create_rent_service_form.is_valid():
            car_service = create_rent_service_form.save(commit=False)
            car_service.user = request.user
            car_service.save()
            return redirect('rent-a-car-posts')

        context = {
            'form': create_rent_service_form
        }
        return render(request, self.template_name, context)


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


class CarServiceDetails(generic.DetailView):
    template_name = 'services/car-service-details.html'
    model = CarService


class RentACarDetails(generic.DetailView):
    template_name = 'services/rent-a-car-details.html'
    model = RentACar


class CarServiceDelete(generic.DeleteView):
    template_name = 'services/cart-service-delete.html'
    model = CarService

    def get_context_data(self, **kwargs):
        context = super(CarServiceDelete, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['pk'] = pk
        return context

    def post(self, request, **kwargs):
        car_service = CarService.objects.get(id=self.kwargs['pk'])
        car_service.delete()
        return redirect('car-services-posts')


class RentACarDelete(generic.DeleteView):
    template_name = 'services/rent-a-car-delete.html'
    model = RentACar

    def get_context_data(self, **kwargs):
        context = super(RentACarDelete, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['pk'] = pk
        return context

    def post(self, request, **kwargs):
        rent_service = RentACar.objects.get(id=self.kwargs['pk'])
        rent_service.delete()
        return redirect('rent-a-car-posts')


class CarServiceEdit(generic.UpdateView):
    template_name = 'services/edit-car-service.html'
    model = CarService
    fields = ('name', 'description', 'time_open', 'time_close', 'location', 'logo')

    def get_success_url(self):
        car_service = CarService.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('car-service-details', kwargs={
            'pk': car_service.id
        })


class RentACarEdit(generic.UpdateView):
    template_name = 'services/edit-rent-a-car.html'
    model = RentACar
    fields = ('name', 'description', 'time_open', 'time_close', 'location', 'logo', 'cars')

    def get_success_url(self):
        rent_a_car = RentACar.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('rent-a-car-details', kwargs={
            'pk': rent_a_car.id
        })
