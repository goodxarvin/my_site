from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    GENDER_CHOICES = (
        ("M", 'male'),
        ("F", "female")
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
