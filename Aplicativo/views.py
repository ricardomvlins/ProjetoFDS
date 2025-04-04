from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Cadastro, Filmes, Favorito
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def homeAdmin(request):
    return render(request, 'homeAdmin.html')

def homeUser(request):
    return render(request, 'homeUser.html')

def login(request):
    next_url = request.GET.get('next')
    
    if request.method == 'POST':
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            
            # Se houver uma URL de redirecionamento e for uma URL válida do nosso site
            if next_url and not next_url.startswith('//') and not next_url.startswith('http'):
                return redirect(next_url)
            
            # Caso contrário, redireciona com base no tipo de usuário
            if user.is_superuser:
                return redirect('homeAdminNomePath')
            else:
                return redirect('homeUserNomePath')
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."
            tipoMensagem = "error"
            return render(request, 'login.html', {
                'mensagem': mensagem, 
                'tipo_mensagem': tipoMensagem,
                'next': next_url
            })
    
    return render(request, 'login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('loginNomePath')

def cadastro(request):
    if request.method == 'POST':
        nomeBD = request.POST.get('nome')
        emailBD = request.POST.get('email')
        senhaBD = request.POST.get('senha')
        confirmarSenhaBD = request.POST.get('confirmarSenha')

        if senhaBD != confirmarSenhaBD:
            mensagem = "As senhas não coincidem. Tente novamente."
            tipoMensagem = "error"
            return render(request, 'cadastro.html', {'mensagem': mensagem, 'tipo_mensagem': tipoMensagem})

        user = User.objects.filter(username=nomeBD).first()

        if user:
            mensagem = "Já existe um usuário com esse nome. Tente novamente"
            tipoMensagem = "error"
            return render(request, 'cadastro.html', {'mensagem': mensagem, 'tipo_mensagem': tipoMensagem})
        else:
            user = User.objects.create_user(username=nomeBD, password=senhaBD)
            user.save()
            mensagem = "Usuário criado com sucesso. Faça o login clicando aqui"
            tipoMensagem = "sucess"
            return render(request, 'cadastro.html', {'mensagem': mensagem, 'tipo_mensagem': tipoMensagem})

    return render(request, 'cadastro.html')

@login_required
def filmes(request):
    if request.method == 'POST':
        nomeFilmeBD = request.POST.get('nomeFilmeInsert')
        diretorFilmeBD = request.POST.get('diretorFilmeInsert')
        anoFilmeBD = request.POST.get('anoFilmeInsert')
        generoFilmeBD = request.POST.get('generoFilmeInsert')

        filmes = Filmes(
            nomeFilmeBD = nomeFilmeBD,
            diretorFilmeBD = diretorFilmeBD,
            anoFilmeBD = anoFilmeBD,
            generoFilmeBD = generoFilmeBD,
        )

        filmes.save()

    return render(request, 'adcFilmeAdmin.html')

@login_required
def visuFilmesUser(request):
    filmes = Filmes.objects.all()
    favoritos = Favorito.objects.filter(usuario=request.user).values_list('filme_id', flat=True)
    return render(request, 'visuFilmeUser.html', {
        'Filmes': filmes,
        'favoritos': list(favoritos)
    })

@login_required
def toggle_favorito(request, filme_id):
    filme = get_object_or_404(Filmes, id=filme_id)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, filme=filme)
    
    if not created:
        favorito.delete()
        return JsonResponse({'status': 'removed'})
    
    return JsonResponse({'status': 'added'})

@login_required
def meus_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('filme')
    return render(request, 'meus_favoritos.html', {'favoritos': favoritos})