from django.db import models

# Create your models here.

#class to store user details
class user_detailss(models.Model):
    #fields
    photo=models.ImageField()
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class query(models.Model):
    #fields
    queryname=models.CharField(max_length=100)
    queryemail=models.CharField(max_length=100)
    querymessage=models.CharField(max_length=1000)
    