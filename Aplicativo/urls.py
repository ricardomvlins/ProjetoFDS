from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('homeUser/', views.homeUser, name='homeUser'),
    path('filmes/', views.filmes, name='filmes'),
    path('visuFilmeUser/', views.visuFilmeUser, name='visuFilmeUser'),
    path('visuFilmeAdmin/', views.visuFilmeAdmin, name='visuFilmeAdmin'),
    path('filme/<int:filme_id>/avaliar/', views.avaliacaoFilmeUser, name='avaliacaoFilmeUser'),
]
