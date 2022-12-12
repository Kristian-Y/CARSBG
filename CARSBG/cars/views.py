from django.shortcuts import render, redirect
from django.views import generic as views
from CARSBG.cars.forms import FilterForm, CreateCarForm
from CARSBG.cars.models import Car


# Create your views here.


class CreateCarAdvert(views.CreateView):
    def get(self, request, *args, **kwargs):
        create_car_form = CreateCarForm()
        context = {
            'form': create_car_form
        }
        return render(request, 'car/create-car-page.html', context)

    def post(self, request, *args, **kwargs):
        create_car_form = CreateCarForm(request.POST, request.FILES)
        print(request.FILES)
        if create_car_form.is_valid():
            print(True)
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
