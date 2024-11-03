from django.db import models
from hospital.models import PatientDetails, HospitalModel
from userApp.models import PatientModel
from hospital.models import DoctorModel


class Prescriptions(models.Model):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalModel,on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

