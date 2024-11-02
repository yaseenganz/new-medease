from django.db import models
from hospital.models import PatientDetails, HospitalModel


class GetPatient(models.Model):
    hospital = models.CharField(editable=False)
    user = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    age = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        if self.user:
            self.hospital = self.user.hospital
            self.age = self.user.age
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.name}   Age: {self.age}  Hospital: {self.hospital}"
