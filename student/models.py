from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
