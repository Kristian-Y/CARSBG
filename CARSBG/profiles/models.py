from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class AppUser(AbstractUser):
    MINIMUM_AGE = 18

    MAX_LEN_USERNAME = 15

    MAX_LEN_PASSWORD = 30

    MAX_LEN_FIRSTNAME = 30
    MAX_LEN_LASTNAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRSTNAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LASTNAME,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
