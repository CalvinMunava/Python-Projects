from django.db import models

# Create your models here.

class Appointment(models.Model):
    StudentNumber = models.CharField(max_length=200,null=False)
    StudentName = models.CharField(max_length=200,null=False)
    AppointmentDate = models.DateField(null=True)
    AppointmentDescription = models.TextField(max_length=1000, null=False)
   

