<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Cadastro, Filmes, Favorito
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
=======
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro, Filmes
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .forms import CadastroForm
>>>>>>> 9cee99f345fbef577cba6acd3aef7d9ecaecf339

def homeAdmin(request):
    return render(request, 'homeAdmin.html')

def homeUser(request):
    return render(request, 'homeUser.html')

<<<<<<< HEAD
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
=======
def login_view(request):
    if request.method == 'POST':
        nomeBD = request.POST.get('nome')
        senhaBD = request.POST.get('senha')

        user = authenticate(request, username=nomeBD, password=senhaBD)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('homeAdmin')
            else:
                return redirect('homeUser')
        else:
            mensagem = "Nome de usuário ou senha inválidos."
            return render(request, 'login.html', {'mensagem': mensagem, 'tipo_mensagem': 'error'})
    else:
        return render(request, 'login.html')
>>>>>>> 9cee99f345fbef577cba6acd3aef7d9ecaecf339

from .forms import CadastroForm
from django.contrib.auth.models import User

from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

<<<<<<< HEAD
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
=======
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirmar_senha = form.cleaned_data['confirmar_senha']
            is_admin = form.cleaned_data.get('is_admin', False)

            if senha != confirmar_senha:
                return render(request, 'cadastro.html', {
                    'form': form,
                    'mensagem': 'As senhas não coincidem.',
                    'tipo_mensagem': 'error'
                })

            if User.objects.filter(username=nome).exists():
                return render(request, 'cadastro.html', {
                    'form': form,
                    'mensagem': 'Nome de usuário já está em uso.',
                    'tipo_mensagem': 'error'
                })

            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
                is_superuser=is_admin,
                is_staff=is_admin
            )
            user.save()
>>>>>>> 9cee99f345fbef577cba6acd3aef7d9ecaecf339

            # Mostra mensagem de sucesso e botão para login
            return render(request, 'cadastro.html', {
                'form': CadastroForm(),  # limpa o formulário
                'mensagem': 'Cadastro realizado com sucesso!',
                'tipo_mensagem': 'success',
                'is_admin': is_admin
            })
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

@login_required
def filmes(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        diretor = request.POST.get('diretor', '').strip()
        ano = request.POST.get('ano', '').strip()
        genero = request.POST.get('genero', '').strip()

<<<<<<< HEAD
        filmes = Filmes(
            nomeFilmeBD = nomeFilmeBD,
            diretorFilmeBD = diretorFilmeBD,
            anoFilmeBD = anoFilmeBD,
            generoFilmeBD = generoFilmeBD,
=======
        if not titulo or not diretor or not ano or not genero:
            mensagem = "Todos os campos são obrigatórios!"
            return render(request, 'adcFilmeAdmin.html', {'mensagem': mensagem, 'tipo_mensagem': 'error'})

        try:
            ano = int(ano)
        except ValueError:
            mensagem = "Ano deve ser um número válido!"
            return render(request, 'adcFilmeAdmin.html', {'mensagem': mensagem, 'tipo_mensagem': 'error'})

        novo_filme = Filmes(
            titulo=titulo,
            diretor=diretor,
            ano=ano,
            genero=genero,
>>>>>>> 9cee99f345fbef577cba6acd3aef7d9ecaecf339
        )
        novo_filme.save()

        mensagem = "Filme cadastrado com sucesso!"
        return render(request, 'adcFilmeAdmin.html', {'mensagem': mensagem, 'tipo_mensagem': 'success'})

    return render(request, 'adcFilmeAdmin.html')

<<<<<<< HEAD
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
=======
def visuFilmeUser(request):
    filmes = Filmes.objects.all()
    return render(request, 'visuFilmeUser.html', {'filmes': filmes})
>>>>>>> 9cee99f345fbef577cba6acd3aef7d9ecaecf339
