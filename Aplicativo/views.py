from django.shortcuts import render
from django.http import HttpResponse
from .models import CadastroAdmin
from .models import CadastroUser
from .models import AdcFilmesAdmin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastroAdmin(request):
    if request.method == 'POST':
        nomeAdminBD = request.POST.get('nomeAdminInsert')
        emailAdminBD = request.POST.get('emailAdminInsert')
        senhaAdminBD = request.POST.get('senhaAdminInsert')
        confirmarSenhaAdminBD = request.POST.get('confirmarSenhaAdminInsert')

        cadastroAdm = CadastroAdmin(
            nomeAdminInsert = nomeAdminBD,
            emailAdminInsert = emailAdminBD,
            senhaAdminInsert = senhaAdminBD,
            confirmarSenhaAdminInsert = confirmarSenhaAdminBD,
        )

        cadastroAdmin.save()

    return render(request, 'cadastroAdmin.html')

def cadastroUser(request):
    if request.method == 'POST':
        nomeUserBD = request.POST.get('nomeUserInsert')
        emailUserBD = request.POST.get('emailUserInsert')
        senhaUserBD = request.POST.get('senhaUserInsert')
        confirmarSenhaUserBD = request.POST.get('confirmarSenhaUserInsert')

        cadastroAdm = CadastroAdmin(
            nomeUserInsert = nomeUserBD,
            emailUserInsert = emailUserBD,
            senhaUserInsert = senhaUserBD,
            confirmarSenhaUserInsert = confirmarSenhaUserBD,
        )

        cadastroUser.save()

    return render(request, 'cadastroUser.html')

def adcFilmesAdmin(request):
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