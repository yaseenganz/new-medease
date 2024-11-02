from django.contrib import admin
from .models import CustomUser,PatientModel

admin.site.register(CustomUser)

class PatinetList(admin.ModelAdmin):
    list_display=['get_username',"get_full_name"]

    def get_username(self,obj):
        return obj.user.username
    
    def get_full_name(self,obj):
        return obj.user.full_name
admin.site.register(PatientModel,PatinetList)