from django.contrib import admin
from . models import DoctorModel, HospitalModel




class DoctorList(admin.ModelAdmin):
    list_display=['id','name','specialization']
admin.site.register(DoctorModel,DoctorList)

class HospitalList(admin.ModelAdmin):
    list_display = ['id','name','phone_number']
admin.site.register(HospitalModel,HospitalList)