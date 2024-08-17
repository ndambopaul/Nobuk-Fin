from django.db import models

from apps.core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_ROLES = (
    ("Admin", "Admin"),
    ("Professional", "Professional"),
    ("Customer", "Customer"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=USER_ROLES)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username