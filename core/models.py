from django.contrib.auth.models import AbstractUser

# from django.db import models


class User(AbstractUser):

    # contact = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
