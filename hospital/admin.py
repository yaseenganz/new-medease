from django.contrib import admin
from . models import DoctorModel, HospitalModel, PatientDetails


class DoctorModelList(admin.ModelAdmin):
    list_display = ('name', 'specialization')
admin.site.register(DoctorModel, DoctorModelList)

class HospitalModelList(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'location')
admin.site.register(HospitalModel, HospitalModelList)

class PatientDetailsList(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'hospital')
admin.site.register(PatientDetails, PatientDetailsList)
