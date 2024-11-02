from django.urls import path
from . import views
urlpatterns =[
    path('register/',views.PatientRegister, name='patient_register'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.log_out,name='log_out'),
    path('dashboard/',views.DashBoard, name="dashboard-view"),
]