from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username_osa = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
