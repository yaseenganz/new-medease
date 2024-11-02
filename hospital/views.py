from django.shortcuts import render,redirect
from .forms import DoctorForm,HospitalForm
from .models import DoctorModel,HospitalModel
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