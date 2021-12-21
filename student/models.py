from django.db import models


class student(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
