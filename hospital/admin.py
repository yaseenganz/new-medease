from django.contrib import admin
from . models import DoctorModel, HospitalModel


admin.site.register(DoctorModel)
admin.site.register(HospitalModel)
