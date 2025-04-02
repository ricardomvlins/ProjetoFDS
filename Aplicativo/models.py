from django.db import models

# Create your models here.

class CadastroAdmin(models.Model):
    nomeBD = models.TextField(null=True, blank=True)
    emailBD = models.EmailField(null=True, blank=True)
    senhaBD = models.TextField(null=True, blank=True)
    confirmarSenhaBD = models.TextField(null=True, blank=True)