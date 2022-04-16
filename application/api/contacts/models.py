from unicodedata import name
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=120)
    phoneNumber = models.CharField(max_length=120)
