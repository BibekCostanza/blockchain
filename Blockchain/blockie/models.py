from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    something=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
