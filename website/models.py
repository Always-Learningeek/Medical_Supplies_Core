from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()
