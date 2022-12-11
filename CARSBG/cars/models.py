from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Car(models.Model):
    MAX_LEN_BRAND = 15
    MAX_LEN_FUEL = 15
    MAX_LEN_MODEL = 30
    MAX_LEN_ENGINE = 30
    MAX_LEN_DESCRIPTION = 150

    car_brand = models.CharField(
        max_length=MAX_LEN_BRAND,
        null=False,
        blank=False,
    )

    car_model = models.CharField(
        max_length=MAX_LEN_MODEL,
        null=False,
        blank=False,
    )

    engine = models.CharField(
        max_length=MAX_LEN_ENGINE,
        null=False,
        blank=False,
    )

    type_of_fuel = models.CharField(
        max_length=MAX_LEN_FUEL,
        null=False,
        blank=False,
    )

    description = models.TextField(
    )

    year = models.IntegerField(
        null=False,
        blank=False,
    )

    price = models.IntegerField(
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    images = models.ImageField(upload_to='img/', )
