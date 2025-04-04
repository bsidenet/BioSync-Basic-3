from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registos.urls')), # Mantenha apenas esta linha para a raiz
]