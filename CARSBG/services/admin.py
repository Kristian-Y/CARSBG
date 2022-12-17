from django.contrib import admin

from CARSBG.services.models import CarService, RentACar


# Register your models here.

@admin.register(CarService)
class CarServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "time_open", "time_close", "user",)
    list_filter = ("id", "name", "time_open", "time_close", "user",)


@admin.register(RentACar)
class RenACarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "time_open", "time_close", "user",)
    list_filter = ("id", "name", "time_open", "time_close", "user",)
