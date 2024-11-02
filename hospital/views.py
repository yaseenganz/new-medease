from django.shortcuts import render
from . models import PatientDetails
from django.http import HttpResponse


def DoctorSignup(request):
    return render(request, 'doctors/index.html')



def create_token(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age  = request.POST.get("age")
        gender = request.POST.get("gender")

        patient = PatientDetails(name=name, age=age, gender=gender)
        patient.save()
        
        return HttpResponse(f"Created Token Successfully {patient.token_number}")
    return render(request, "token/token.html")
