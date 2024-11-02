from django.db import models
from hospital.models import PatientDetails, HospitalModel
from userApp.models import PatientModel
from hospital.models import DoctorModel




class Prescription(models.Model):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalModel,on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class GetPatient(models.Model):
    user = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.user:
            self.hospital = self.user.hospital
            self.age = self.user.age
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.name}   Age: {self.age}  Hospital: {self.hospital}"


