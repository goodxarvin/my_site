from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender_choices = [
        ("m", 'male'),
        ("f", "female")
    ]
    gender = models.CharField(
        max_length=1, choices=gender_choices, null=True, blank=True)
