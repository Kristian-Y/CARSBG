from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

UserModel = get_user_model()


class CarService(models.Model):
    CITY_MAX_LEN = 255
    NAME_MAX_LEN = 30
    MAX_LEN_LOCATION = 100

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    time_open = models.TimeField(
        null=False,
        blank=False
    )
    time_close = models.TimeField(
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        null=False,
        blank=False
    )

    logo = models.URLField(
        null=False,
        blank=False
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


class RentACar(models.Model):
    NAME_MAX_LEN = 30
    MAX_LEN_LOCATION = 100

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False
    )

    cars = models.TextField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    logo = models.URLField(
        null=False,
        blank=False,
    )

    time_open = models.TimeField(
        null=False,
        blank=False,
    )

    time_close = models.TimeField(
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        null=False,
        blank=False
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
