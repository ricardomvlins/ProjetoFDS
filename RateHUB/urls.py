from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicativo.urls')),  # Substitua "core" pelo nome real da sua app
]
