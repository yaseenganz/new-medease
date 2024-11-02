from django import forms
from .models import CustomUser
from .models import DoctorModel, PatientDetails

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
            
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already registered")


class tokenCreation(forms.ModelForm):
    class Meta:
        modle = PatientDetails
        files = ['name', 'age', 'gender']
        