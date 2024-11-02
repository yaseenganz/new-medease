
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/',include('userApp.urls')),
    # path('token/', include('tokenSystem.urls'), name='token_verification'),
    path('doctor/', include('hospital.urls')),
    path('hospital/',include('hospital.urls'))
]
