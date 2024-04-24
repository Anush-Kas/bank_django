from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        DIRECTOR = "DIRECTOR", "DIRECTOR"
        ACCOUNTANT = "ACCOUNTANT", "ACCOUNTANT"
        MANAGER = "MANAGER", "MANAGER"
        CLIENT = "CLIENT", "CLIENT"

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.CLIENT
    )

