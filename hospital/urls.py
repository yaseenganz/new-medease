from django.urls import path
from . import views
urlpatterns = [
    path('sign-up/',views.DoctorSignup,name="doctor_signup"),
    path('register/',views.HospitalRegistration,name="hospital_form"),
    path('create_token/', views.create_token),
]