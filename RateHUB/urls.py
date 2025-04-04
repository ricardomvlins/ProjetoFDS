from django.urls import path, include
from Aplicativo import views

urlpatterns = [
    path('',views.home, name='homeNomePath'),
    path('Cadastro_Admin/', views.cadastroAdmin ,name='cadastroAdmNomePath'),
    path('Cadastro_User/', views.cadastroUser ,name='cadastroUserNomePath'),
    path('Adicionar_Filmes_Admin/', views.adcFilmesAdmin, name='adcFilmesAdmNomePath'),
]
