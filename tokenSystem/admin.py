from django.contrib import admin
from . models import PatientDetails


# class PatientDetailsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'gender', 'token_number')
#     search_fields = ('name', 'gender')

admin.site.register(PatientDetails)


