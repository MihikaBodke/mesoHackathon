from pydoc import pathdirs
from django.db import models

# Create your models here.

class Patient(models.Model):

    name = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    mail = models.EmailField()
    password = models.CharField(max_length=20)

class Doctor(models.Model):
    name = models.CharField(max_length=20)

class Appointment(models.Model):
    patient = models.ForeignKey(  Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey( Doctor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = models.CharField(max_length=100)
    mode = models.CharField(max_length=20) #virtual or inperson
    amount = models.CharField(max_length=10)

class Hospital(models.Model):
    name = models.CharField(max_length=50)

