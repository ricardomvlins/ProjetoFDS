from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('Home_Admin/', views.homeAdmin, name='homeAdminNomePath'),
    path('Home_User/', views.homeUser, name='homeUserNomePath'),
    path('', views.login, name='loginNomePath'),
    path('Cadastro/', views.cadastro, name='cadastroNomePath'),
    path('Adicionar_Filmes_Admin/', views.filmes, name='adcFilmesAdmNomePath'),
    path('Visualizar_Filmes_User/', views.visuFilmesUser, name='visuFilmesUserNomePath'),
    path('toggle-favorito/<int:filme_id>/', views.toggle_favorito, name='toggle_favorito'),
    path('meus-favoritos/', views.meus_favoritos, name='meus_favoritos'),
    path('logout/', views.logout_view, name='logout'),
] 
=======
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('homeUser/', views.homeUser, name='homeUser'),
    path('filmes/', views.filmes, name='filmes'),
    path('visuFilmeUser/', views.visuFilmeUser, name='visuFilmeUser'),
]
>>>>>>> 9cee99f345fbef577cba6acd3aef7d9ecaecf339
