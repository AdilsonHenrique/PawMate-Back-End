from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilPawmate

class PerfilPawmateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = PerfilPawmate
        fields = ['nome_dono', 'cidade_dono', 'estado_dono', 'pais_dono', 'telefone_dono',
                  'nome_animal', 'idade_animal', 'raca_animal', 'password']

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']