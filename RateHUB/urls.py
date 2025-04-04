from django.contrib import admin
from django.urls import path
from Aplicativo import views

urlpatterns = [
    path('Home_Admin/', views.homeAdmin, name='homeAdminNomePath'),
    path('Home_User/', views.homeUser, name='homeUserNomePath'),
    path('', views.login, name='loginNomePath'),
    path('Cadastro/', views.cadastro, name='cadastroNomePath'),
    path('Adicionar_Filmes_Admin/', views.filmes, name='adcFilmesAdmNomePath'),
    path('Visualizar_Filmes_User/', views.visuFilmesUser, name='visuFilmesUserNomePath'),
    path('toggle-favorito/<int:filme_id>/', views.toggle_favorito, name='toggle_favorito'),
    path('meus-favoritos/', views.meus_favoritos, name='meus_favoritos'),
    path('logout/', views.logout_view, name='logout'),
    path('Banco_Dados/', admin.site.urls),
]
