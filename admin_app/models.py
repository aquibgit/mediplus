from django.db import models

# Create your models here.
class doctor_detailss(models.Model):
    #fields
    doctorphoto=models.ImageField()
    doctorname=models.CharField(max_length=100)
    doctoremail=models.CharField(max_length=100)
    doctorphone=models.CharField(max_length=100)
    doctorpayment=models.CharField(max_length=100)
    doctorhours=models.CharField(max_length=100)
    doctorspecialisation=models.CharField(max_length=100)