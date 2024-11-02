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

    def __str__(self):
        return self.name


class HospitalModel(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10,unique=True)
    location = models.TextField()
    doctors = models.ManyToManyField(DoctorModel, related_name="hospitals", blank=True)
    license_number = models.CharField(max_length=6)

    def __str__(self):
        return self.name
    

class PatientDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hospital = models.ForeignKey(HospitalModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    token_number = models.PositiveIntegerField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.token_number:
            last_token = PatientDetails.objects.order_by('-token_number').first()
            self.token_number = last_token.token_number + 1 if last_token else 1 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name