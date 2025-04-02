from django.urls import path, include
from Aplicativo import views

urlpatterns = [
    path('', views.cadastroAdm ,name='cadastroAdmNomePath'),
]
