from django.urls import path, include
from Aplicativo import views
from django.contrib import admin

urlpatterns = [
    path('Home_Admin/',views.homeAdmin, name='homeAdminNomePath'),
    path('Home_User/',views.homeUser, name='homeUserNomePath'),
    path('', views.login, name='loginNomePath'),
    path('Cadastro/', views.cadastro, name='cadastroNomePath'),
    path('Adicionar_Filmes_Admin/', views.filmes, name='adcFilmesAdmNomePath'),
    path('Visualizar_Filmes_User/', views.visuFilmesUser, name='visuFilmesUserNomePath'),
    path('Banco_Dados/', admin.site.urls),
]
