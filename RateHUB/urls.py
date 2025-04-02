
from django.urls import path, include
from Aplicativo import views

urlpatterns = [
    path('', views.home, name='home'),
]
