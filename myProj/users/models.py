from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField()
    bio = models.TextField(null=True)

    def __str__(self):
        return self.username
