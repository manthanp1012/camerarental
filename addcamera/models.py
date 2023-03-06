from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.


class AddCamera(models.Model):
    camera_photo = models.FileField(upload_to='media')
    camera_name = models.CharField(max_length=30)
    camera_desc = models.TextField()
    camera_price = models.IntegerField()

    def __str__(self):
        return self.camera_desc


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    feedback = models.TextField(max_length=100)

    def __str__(self):
        return self.name
