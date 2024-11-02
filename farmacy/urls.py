from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:pk>',views.Pharmacy_register,name='pharmacy_signup'),
    # path('get_prescription/', views.get_pre),
]