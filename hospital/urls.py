from django.urls import path
from . import views
urlpatterns = [
    path('sign-up/',views.DoctorSignup,name="doctor_signup"),
    path('register/',views.HospitalRegistration,name="hospial_form")
]