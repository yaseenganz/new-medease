from django import forms
from .models import CustomUser
from .models import DoctorModel, PatientDetails,  HospitalModel

class DoctorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    specialization = forms.ChoiceField(
        choices=DoctorModel.SPECIALIZATION_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Specialization'}),
    )
    class Meta:
        model = CustomUser
        fields = ['full_name','email','phone_number','specialization']
        widgets={
            'full_name':forms.TextInput(attrs={'placeholder':'Full Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email'}),
            'phone_number':forms.TextInput(attrs={'placeholder':'Phone Number'})
        }

        def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            if not phone_number.isdigit():
                raise forms.ValidationError("Phone number must contain only digits.")
            elif CustomUser.objects.filter(phone_number=phone_number).exists():
                raise forms.ValidationError("This number already registerd")
            
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already registered")


class tokenCreation(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['name', 'age', 'gender', 'doctor', 'hospital']
            

class HospitalForm(forms.ModelForm):
    class Meta:
        model = HospitalModel
        fields = ['name', 'phone_number', 'location', 'license_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        
        
        if HospitalModel.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This number is already registered.")
        
        return phone_number
