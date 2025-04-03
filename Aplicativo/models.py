from django.db import models

# Create your models here.

class CadastroAdmin(models.Model):
    nomeAdminBD = models.TextField(null=True, blank=True)
    emailAdminBD = models.EmailField(null=True, blank=True)
    senhaAdminBD = models.TextField(null=True, blank=True)
    confirmarSenhaAdminBD = models.TextField(null=True, blank=True)

class CadastroUser(models.Model):
    nomeUserBD = models.TextField(null=True, blank=True)
    emailUserBD = models.EmailField(null=True, blank=True)
    senhaUserBD = models.TextField(null=True, blank=True)
    confirmarSenhaUserBD = models.TextField(null=True, blank=True)

class AdcFilmesAdmin(models.Model):
    nomeFilmeBD = models.TextField(null=True, blank=True)
    diretorFilmeBD = models.TextField(null=True, blank=True)
    anoFilmeBD = models.IntegerField(null=True, blank=True)
    generoFilmeBD = models.TextField(null=True, blank=True)
