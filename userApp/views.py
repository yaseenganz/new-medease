from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import PatientSignup
from .models import PatientModel,CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect

User = get_user_model()


def main_page(request):
    return render(request, "mainpages/main_page.html")

@login_required(login_url="")
def DashBoard(request):
    return render(request,'home.html')

@csrf_exempt
def PatientRegister(request):
    if request.method == "POST":
        form = PatientSignup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            if not user.username:
                user.username = form.cleaned_data['email']  
            user.save()
            PatientModel.objects.create(user=user)  
            auth_login(request, user) 
            return redirect('dashboard-view')
    else:
        form = PatientSignup()  

    context = {
        "title": "Signup",
        "form": form,  
    }
    return render(request, 'signup.html', context=context)



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request): 
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email,password)
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard-view')
        else:
            # If authentication fails, send an error message to the template
            context = {
                "title": "Login",
                "error": "Invalid login credentials. Please try again."
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')


def log_out(request):
    auth_logout(request)
    return redirect('login_view')