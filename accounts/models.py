from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/',default='default.png')
    description = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=False)

    def __str__(self):
        return f'{self.user.username} Profile'
