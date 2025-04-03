from django.shortcuts import render
from django.http import HttpResponse
from .models import CadastroAdmin
from .models import AdcFilmesAdmin

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

def adcFilmesAdm(request):
    if request.method == 'POST':
        nomeFilmeBD = request.POST.get('nomeFilmeInsert')
        diretorFilmeBD = request.POST.get('diretorFilmeInsert')
        anoFilmeBD = request.POST.get('anoFilmeInsert')
        generoFilmeBD = request.POST.get('generoFilmeInsert')

        adcFilmesAdm = AdcFilmesAdmin(
            nomeFilmeInsert = nomeFilmeBD,
            diretorFilmeInsert = diretorFilmeBD,
            anoFilmeInsert = anoFilmeBD,
            generoFilmeInsert = generoFilmeBD,
        )

        adcFilmesAdm.save()

    return render(request, 'adcFilmeAdmin.html')