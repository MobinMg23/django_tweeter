from django.db import models
from django_app.models.user.user import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    bio = models.TextField(max_length=200)
    # photo = models.ImageField()

    def __str__(self):
        return f'{self.user.username}'