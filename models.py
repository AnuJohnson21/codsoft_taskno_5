from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class contacts(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)


class calculator(models.Model):
    number1=models.IntegerField()
    number2=models.IntegerField()
    operation=models.CharField(max_length=20)


class passwordgenerator(models.Model):
    length = models.IntegerField()

