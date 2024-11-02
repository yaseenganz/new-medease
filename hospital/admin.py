from django.contrib import admin
from . models import DoctorModel, HospitalModel, PatientDetails


class DoctorModelList(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization')
admin.site.register(DoctorModel, DoctorModelList)

class HospitalModelList(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
admin.site.register(HospitalModel, HospitalModelList)

class PatientDetailsList(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'hospital','token_number')
admin.site.register(PatientDetails, PatientDetailsList)

