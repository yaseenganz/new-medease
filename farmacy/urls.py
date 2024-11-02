from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.Pharmacy_register,name='pharmacy_signup'),
]