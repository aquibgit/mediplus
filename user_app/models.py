from django.db import models

# Create your models here.
class appointment_details(models.Model):
    #fields
    user_id=models.CharField(max_length=100)
    patient_name=models.CharField(max_length=100)
    patient_email=models.CharField(max_length=100)
    patient_phone=models.CharField(max_length=100)
    patient_age=models.CharField(max_length=100)
    booking_date=models.CharField(max_length=100)
    doctor_name=models.CharField(max_length=100)
    patient_problem=models.CharField(max_length=1000)