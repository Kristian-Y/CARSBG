from django.contrib import admin

from CARSBG.services.models import CarService, RentACar


# Register your models here.

@admin.register(CarService)
class CarServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(RentACar)
class RenACarAdmin(admin.ModelAdmin):
    pass

