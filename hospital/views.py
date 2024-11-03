from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import DoctorForm,HospitalForm, tokenCreation
from .models import DoctorModel, HospitalModel, PatientDetails
from django.contrib.auth import authenticate, login as auth_login


def DoctorSignup(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.set_password(form.cleaned_data['password'])
            doctor.username = form.cleaned_data['email']
            doctor.save()
            DoctorModel.objects.create(
                doctor=doctor,
                name=doctor.full_name,
                specialization=form.cleaned_data['specialization']
            )
            authenticated_doctor = authenticate(request,username=form.cleaned_data['email'],password=form.cleaned_data['password'])
            auth_login(request,authenticated_doctor)
            return redirect('dashboard-view')
    else:
        form = DoctorForm()

    context = {"form": form}
    return render(request, 'doctors/index.html', context)

def HospitalRegistration(request):
    if request.method == "POST":
        form = HospitalForm(request.POST) 
        if form.is_valid():
            hospital = form.save()  
            return redirect('dashboard-view')
    else:
        form = HospitalForm() 

    context = {
        "form": form
    }
    return render(request, "hospital/index.html", context=context)



def create_token(request):
    if request.method == "POST":
        form = tokenCreation(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            doctor = form.cleaned_data['doctor']
            hospital = form.cleaned_data['hospital']
            
            instance = PatientDetails.objects.create(name=name, age=age, gender=gender, doctor=doctor, hospital=hospital)
            instance.save()
        return render(request, "mainpages/success_page.html")
    else:
        form = tokenCreation()
        

    return render(request, "mainpages/token_creation.html", { 'form': form })