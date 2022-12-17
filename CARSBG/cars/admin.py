from django.contrib import admin

from CARSBG.cars.models import Car


# Register your models here.

@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ("id", "car_brand", "car_model", "user", )
    list_filter = ("year",)
