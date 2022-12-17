from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from CARSBG.cars.forms import FilterForm, CreateCarForm
from CARSBG.cars.models import Car


# Create your views here.


class CreateCarAdvert(views.CreateView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            create_car_form = CreateCarForm()
            context = {
                'form': create_car_form
            }
            return render(request, 'car/create-car-page.html', context)
        else:
            return redirect('index')

    def post(self, request, *args, **kwargs):
        create_car_form = CreateCarForm(request.POST, request.FILES)
        if create_car_form.is_valid():
            car = create_car_form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('catalogue')

        context = {
            'form': create_car_form
        }
        return render(request, 'car/create-car-page.html', context)


class Catalogue(views.CreateView):
    def get(self, request, *args, **kwargs):
        filter_form = FilterForm()
        cars = Car.objects.all()
        context = {
            'filter_form': filter_form,
            'cars': cars
        }
        return render(request, 'catalogue.html', context)

    def post(self, request, *args, **kwargs):
        filter_form = FilterForm(request.POST)
        cars = Car.objects.all()
        filtered_cars = []
        if filter_form.is_valid():
            print(filter_form.data['brand'])
            for car in cars:
                if car.car_brand == filter_form.data['brand']:
                    filtered_cars.append(car)

        filter_form = FilterForm()
        context = {
            'filter_form': filter_form,
            'cars': filtered_cars
        }
        return render(request, 'catalogue.html', context)


class MyCars(views.CreateView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            filter_form = FilterForm()
            cars = Car.objects.all()
            filtered_cars = []
            for car in cars:
                if car.user == self.request.user:
                    filtered_cars.append(car)

            context = {
                'filter_form': filter_form,
                'cars': cars
            }
            return render(request, 'car/my-cars.html', context)
        else:
            return redirect('index')


def advert(request):
    return render(request, 'base/advert.html')


class CarDetails(views.CreateView):
    def get(self, request, *args, **kwargs):
        car_id = kwargs.get('pk')
        car = Car.objects.get(id=car_id)

        context = {
            'car': car
        }
        return render(request, 'car/car-details.html', context)


class CarDelete(views.DeleteView):
    template_name = 'car/car-delete.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDelete, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['pk'] = pk
        return context

    def post(self, request, **kwargs):
        rent_service = Car.objects.get(id=self.kwargs['pk'])
        rent_service.delete()
        return redirect('catalogue')


class CarEdit(views.UpdateView):
    template_name = 'car/edit-car.html'
    model = Car
    fields = ('car_brand', 'car_model', 'engine', 'type_of_fuel', 'description', 'images', 'year', 'price')

    def get_success_url(self, **kwargs):
        car = Car.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('car details', kwargs={
            'pk': car.id
        })
