from django import forms
from .models import Pharmacy

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = ['phone_number', 'pharmacy_name', 'license_number'] 

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if Pharmacy.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This number is already registered.")
        return phone_number
    
    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number") 
        if Pharmacy.objects.filter(license_number=license_number).exists():
            raise forms.ValidationError("This license number is already registered.")
        return license_number
