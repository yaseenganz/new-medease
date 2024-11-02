from django.db import models
from userApp.models import CustomUser


class DoctorModel(models.Model):
    doctor = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    
    SPECIALIZATION_CHOICES = (
        ('cardio', 'Cardiology'),
        ('dermo', 'Dermatology'),
        ('pedia', 'Pediatrics'),
        ('psy', 'Psychiatry'),
        ('other', 'Other'),
    )
    specialization = models.CharField(max_length=10, choices=SPECIALIZATION_CHOICES)

    def str(self):
        return self.name


class HospitalModel(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10, unique=True)
    location = models.TextField()
    doctors = models.ManyToManyField(DoctorModel, related_name="hospitals", blank=True)
    license_number = models.CharField(max_length=6)

    def str(self):
        return self.name