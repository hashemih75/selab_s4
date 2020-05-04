from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField()
    bio = models.TextField(null=True)

    REQUIRED_FIELDS = [
        'birth_date',
        'email'
    ]

    def __str__(self):
        return self.username
