from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    comments = models.TextField(max_length=1000)

class RegisterYourHouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phonenumber = models.IntegerField()
    postalcode = models.CharField(max_length=10)


