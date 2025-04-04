from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro, Filmes
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .forms import CadastroForm

def homeAdmin(request):
    return render(request, 'homeAdmin.html')

def homeUser(request):
    return render(request, 'homeUser.html')

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

from .forms import CadastroForm
from django.contrib.auth.models import User

from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

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

def filmes(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        diretor = request.POST.get('diretor', '').strip()
        ano = request.POST.get('ano', '').strip()
        genero = request.POST.get('genero', '').strip()

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
        )
        novo_filme.save()

        mensagem = "Filme cadastrado com sucesso!"
        return render(request, 'adcFilmeAdmin.html', {'mensagem': mensagem, 'tipo_mensagem': 'success'})

    return render(request, 'adcFilmeAdmin.html')

def visuFilmeUser(request):
    filmes = Filmes.objects.all()
    return render(request, 'visuFilmeUser.html', {'filmes': filmes})
