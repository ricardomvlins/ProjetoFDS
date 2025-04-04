from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comentario, Filmes
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

def homeAdmin(request):
    return render(request, 'homeAdmin.html')

def homeUser(request):
    return render(request, 'homeUser.html')

def login(request):
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

    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')
        is_admin = request.POST.get('is_admin') == 'on' 

        if senha != confirmar_senha:
            return render(request, 'cadastro.html', {
                'mensagem': 'As senhas não coincidem.',
                'tipo_mensagem': 'error'
            })

        if User.objects.filter(username=nome).exists():
            return render(request, 'cadastro.html', {
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

        return render(request, 'cadastro.html', {
            'mensagem': 'Cadastro realizado com sucesso!',
            'tipo_mensagem': 'success'
        })

    return render(request, 'cadastro.html')

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

def avaliacaoFilmeUser(request, filme_id):
    filme = get_object_or_404(Filmes, id=filme_id)
    comentarios = Comentario.objects.filter(filme=filme).order_by('-id')  # Buscar os comentários do filme

    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        nota = request.POST.get('nota')
        Comentario.objects.create(
            usuario=request.user,
            filme=filme,
            texto=comentario,
            nota=nota
        )
        return redirect('avaliacaoFilmeUser', filme_id=filme.id)

    return render(request, 'avaliacaoFilmeUser.html', {
        'filme': filme,
        'comentarios': comentarios 
    })

def visuFilmeAdmin(request):
    filmes = Filmes.objects.all()

    return render(request, 'visuFilmeAdmin.html', {'filmes': filmes})