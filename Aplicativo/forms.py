from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label='Nome de usuário')
    email = forms.EmailField(required=True, label='Email')
    senha = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirmar Senha')
    is_admin = forms.BooleanField(required=False, label='Cadastrar como administrador')

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if User.objects.filter(username=nome).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return nome

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar = cleaned_data.get("confirmar_senha")

        if senha and confirmar and senha != confirmar:
            raise forms.ValidationError("As senhas não coincidem.")
