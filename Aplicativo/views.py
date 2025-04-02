from django.shortcuts import render
from django.http import HttpResponse
from .models import CadastroAdmin

# Create your views here.

def cadastroAdm(request):
    if request.method == 'POST':
        nomeBD = request.POST.get('nomeInsert')
        emailBD = request.POST.get('emailInsert')
        senhaBD = request.POST.get('senhaInsert')
        confirmarSenhaBD = request.POST.get('confirmarSenhaInsert')

        cadastroAdm = CadastroAdmin(
            nomeInsert = nomeBD,
            emailInsert = emailBD,
            senhaInsert = senhaBD,
            confirmarSenhaInsert = confirmarSenhaBD,
        )

        cadastroAdm.save()

    return render(request, 'cadastroAdmin.html')