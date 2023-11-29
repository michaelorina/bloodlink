from django.db import models
from django.db.models import Model


# Create your models here.

class Donors(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    dob = models.DateField(null=True)
    organization = models.CharField(max_length=40, null=True)
    location = models.CharField(max_length=40, null=True)
    bloodgroup = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
