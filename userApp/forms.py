from django import forms
from .models import CustomUser,PatientModel

class PatientSignup(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name','email','phone_number','password']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


                
        
