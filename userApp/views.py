from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import PatientSignup
User = get_user_model()

def PatientRegister(request):
    if request.metod == "POST":
        form = PatientSignup()
    context={
        'title':"SignUp",
        'form':form
    }
    return render(request,'index.html',context=context)