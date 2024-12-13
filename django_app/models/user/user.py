from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.username}'