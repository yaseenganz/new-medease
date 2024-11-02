from django.urls import path
from . import views
urlpatterns =[
    path('create_token/', views.create_token, name='create_token'),
]