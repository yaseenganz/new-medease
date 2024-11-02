from django import forms
from .models import Prescriptions
from hospital.models import PatientDetails

class SubmitPrescription(forms.ModelForm):
    token_number = forms.IntegerField(help_text="Enter token number")

    class Meta:
        model = Prescriptions
        fields = ['text']

    def clean_token_number(self):
        token_number = self.cleaned_data.get('token_number')
        if not PatientDetails.objects.filter(token_number=token_number).exists():
            raise forms.ValidationError("Invalid token number. Patient not found.")
        return token_number
