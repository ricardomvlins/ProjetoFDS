from django.db import models
from django.contrib.auth.models import User

class Cadastro(models.Model):
    nome = models.CharField(max_length=100, default='usuario_temp')
    email = models.EmailField(default='temp@email.com')
    senha = models.CharField(max_length=100, default='senha123')

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    GENERO_CHOICES = [
        ('acao', 'Ação'),
        ('terror', 'Terror'),
        ('comedia', 'Comédia'),
        ('ficcao-cientifica', 'Ficção Científica'),
        ('romance', 'Romance'),
        ('heroi', 'Herói'),
        ('suspense', 'Suspense'),
        ('drama', 'Drama'),
        ('aventura', 'Aventura'),
        ('historia', 'História'),
        ('documentario', 'Documentário'),
        ('guerra', 'Guerra'),
        ('fantasia', 'Fantasia'),
        ('biografia', 'Biografia'),
        ('esporte', 'Esporte'),
    ]

    TIPO_CHOICES = [
        ('live-action', 'Live Action'),
        ('animacao', 'Animação'),
    ]   

    titulo = models.CharField(max_length=100, default='Título não informado')
    diretor = models.CharField(max_length=100, default='Diretor não informado')
    ano = models.IntegerField(default=1900)
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    sinopse = models.TextField(default='Sinopse não informada.')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    texto = models.TextField()
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(6)])  
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.filme.titulo} - {self.nota} estrelas"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'filme') 

    def __str__(self):
        return f"{self.usuario.username} favoritou {self.filme.titulo}"

    