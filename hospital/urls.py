from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.DoctorSignup,name="doctor_signup")
]