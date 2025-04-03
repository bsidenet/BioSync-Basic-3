from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blood_pressure/', include('blood_pressure.urls')),
]