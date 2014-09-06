from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=128)
    session = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
