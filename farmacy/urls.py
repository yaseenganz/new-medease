from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:pk>/', views.Pharmacy_register, name='pharmacy_signup'),
    path('get_link/', views.get_link, name='get_link'),  # Assuming this is to retrieve some prescription or link data
    path('scan_qr/', views.sent_data, name='sent_data'),  # Endpoint to trigger QR scan and return data
]
