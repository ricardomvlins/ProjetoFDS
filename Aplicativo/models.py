from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nomeBD = models.TextField(null=True, blank=True)
    emailBD = models.EmailField(null=True, blank=True)
    senhaBD = models.TextField(null=True, blank=True)
    confirmarSenhaBD = models.TextField(null=True, blank=True)

class Filmes(models.Model):
    nomeFilmeBD = models.TextField(null=True, blank=True)
    diretorFilmeBD = models.TextField(null=True, blank=True)
    anoFilmeBD = models.IntegerField(null=True, blank=True)
    generoFilmeBD = models.TextField(null=True, blank=True)
