from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Name:")
    last_name = models.CharField(max_length=100, verbose_name="Surname:")
    email = models.EmailField(max_length=100, verbose_name="Email:")
    phone = models.CharField(max_length=100, verbose_name="Phone number:")
    message = models.TextField(blank=True, verbose_name="Message:")

    def __str__(self):
        return self.email