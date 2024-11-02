from django.contrib import admin
from  .models import Pharmacy
# Register your models here.


class PharmacyList(admin.ModelAdmin):
    list_display=["id","pharmacy_name","license_number"]

admin.site.register(Pharmacy,PharmacyList)