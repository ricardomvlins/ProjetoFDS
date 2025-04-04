from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100, default='usuario_temp')
    email = models.EmailField(default='temp@email.com')
    senha = models.CharField(max_length=100, default='senha123')

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    titulo = models.CharField(max_length=100, default='Título não informado')
    diretor = models.CharField(max_length=100, default='Diretor não informado')
    ano = models.IntegerField(default=1900)
    genero = models.CharField(max_length=50, default='Gênero não informado')

    def __str__(self):
        return self.titulo
