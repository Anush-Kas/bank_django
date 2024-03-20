from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        DIRECTOR = "DIRECTOR", "Director"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"
        MANAGER = "MANAGER", "Manager"
        CLIENT = "CLIENT", "Client"

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.CLIENT
    )

