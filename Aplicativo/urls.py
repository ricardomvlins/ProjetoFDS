from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('homeUser/', views.homeUser, name='homeUser'),
    path('filmes/', views.filmes, name='filmes'),
    path('visuFilmeUser/', views.visuFilmeUser, name='visuFilmeUser'),
    path('visuFilmeAdmin/', views.visuFilmeAdmin, name='visuFilmeAdmin'),
    path('filmes/<int:filme_id>/avaliar/', views.avaliacaoFilmeUser, name='avaliacaoFilmeUser'),
    path('filmes/<int:filme_id>/visuComentarios/', views.visuComentariosAdmin, name='visuComentariosAdmin'),
    path('comentario/<int:comentario_id>/deletarComentario', views.deletarComentarioAdmin, name='deletarComentarioAdmin'),
    path('filmes/<int:filme_id>/favoritar', views.favoritarFilme, name='favoritarFilme'),
    path('verFavoritos/', views.verFavoritos, name='verFavoritos'),
    path('sair/', views.sair, name='sair'),
    path('filmes/<int:filme_id>/verMaisFilmeAdmin', views.verMaisFilmeAdmin, name='verMaisFilmeAdmin'),
    path('filmes/<int:filme_id>/verMaisFilmeUser', views.verMaisFilmeUser, name='verMaisFilmeUser'),
    path('filmes/<int:filme_id>/deletarFilmeAdmin', views.deletarFilmeAdmin, name='deletarFilmeAdmin'),
    path('recomendacoes/', views.recomendacoes, name='recomendacoes'),
    path('filmes/<int:filme_id>/editarFilmeAdmin', views.editarFilmeAdmin, name='editarFilmeAdmin'),
    path('filmes/buscarFilmeUser/', views.buscarFilmeUser, name='buscarFilmeUser'),
    path('filmes/buscarFilmeAdmin/', views.buscarFilmeAdmin, name='buscarFilmeAdmin'),
    path('filmes/verMaisMissaoImpossivelUser', views.verMaisMissaoImpossivelUser, name='verMaisMissaoImpossivelUser'),
    path('filmes/verMaisLilo&StitchUser', views.verMaisLiloStitchUser, name='verMaisLiloStitchUser'),
    path('filmes/verMaisPremonicaoUser', views.verMaisPremonicaoUser, name='verMaisPremonicaoUser'),
    path('filmes/verMaisThunderboltsUser', views.verMaisThunderboltsUser, name='verMaisThunderboltsUser'),
    path('filmes/verMaisMissaoImpossivelAdmin', views.verMaisMissaoImpossivelAdmin, name='verMaisMissaoImpossivelAdmin'),
    path('filmes/verMaisLilo&StitchAdmin', views.verMaisLiloStitchAdmin, name='verMaisLiloStitchAdmin'),
    path('filmes/verMaisPremonicaoAdmin', views.verMaisPremonicaoAdmin, name='verMaisPremonicaoAdmin'),
    path('filmes/verMaisThunderboltsAdmin', views.verMaisThunderboltsAdmin, name='verMaisThunderboltsAdmin'),
]
