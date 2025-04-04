from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro
from .models import Filmes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def homeAdmin(request):
    return render(request, 'homeAdmin.html')

def homeUser(request):
    return render(request, 'homeUser.html')

def login(request):
    if request.method == 'POST':
        nomeBD = request.POST.get('nome')
        emailBD = request.POST.get('email')
        senhaBD = request.POST.get('senha')
        confirmarSenhaBD = request.POST.get('confirmarSenha')

        user = authenticate(request, username=nomeBD, password=senhaBD)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('homeAdmin') 
            else:
                return redirect('homeUser')   
        
        else:
            mensagem = "Alguma informação está inválida. Tente novamente"
            tipoMensagem = "error"
            return render(request, 'login.html', {'mensagem': mensagem, 'tipo_mensagem': tipoMensagem})
    else:
        return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        nomeBD = request.POST.get('nome')
        emailBD = request.POST.get('email')
        senhaBD = request.POST.get('senha')
        confirmarSenhaBD = request.POST.get('confirmarSenha')

        user = User.objects.filter(username=nomeBD).first()

        if user:
            mensagem = "Já existe um usuário com esse nome. Tente novamente"
            tipoMensagem = "error"
            return render(request, 'cadastro.html', {'mensagem': mensagem, 'tipo_mensagem':tipoMensagem})

        else:
            user = User.objects.create_user(username=nomeBD, password=senhaBD)
            user.save()
            mensagem = "Usuário criado com sucesso. Faça o login clicando aqui"
            tipoMensagem = "sucess"

    return render(request, 'cadastro.html')

def filmes(request):
    if request.method == 'POST':
        nomeFilmeBD = request.POST.get('nomeFilmeInsert')
        diretorFilmeBD = request.POST.get('diretorFilmeInsert')
        anoFilmeBD = request.POST.get('anoFilmeInsert')
        generoFilmeBD = request.POST.get('generoFilmeInsert')

        filmes = Filmes(
            nomeFilmeInsert = nomeFilmeBD,
            diretorFilmeInsert = diretorFilmeBD,
            anoFilmeInsert = anoFilmeBD,
            generoFilmeInsert = generoFilmeBD,
        )

        filmes.save()

    return render(request, 'adcFilmeAdmin.html')

def visuFilmesUser(request):
    filmes = Filmes.objects.all()
    return render(request, 'visuFilmeUser.html',{'Filmes': filmes})