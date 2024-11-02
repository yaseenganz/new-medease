
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/',include('userApp.urls')),
    path('doctor/', include('hospital.urls')),
    path('hospital/',include('hospital.urls')),

    path('pharmacy/',include('farmacy.urls')),



    path('prescription/', include('prescription.urls')),

]
