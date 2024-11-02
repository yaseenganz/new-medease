from django.db import models


class DoctorInfo(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    licence_number = models.CharField(max_length=100)
    medicine = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.doctor_name

class PatiantInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
