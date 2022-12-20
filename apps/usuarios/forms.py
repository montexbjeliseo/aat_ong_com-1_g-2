from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Usuario
from django.db import models

class RegisterUserForm(UserCreationForm):
    username = CharField(label='Nombre de usuario', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de usuario'}))
    email = EmailField(label='Email', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'}))
    first_name = CharField(label='Nombre', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre'}))
    last_name = CharField(label='Apellido', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apellido'}))
    password1 = CharField(
        label='Contraseña', widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'}), required=True)
    password2 = CharField(
        label='Confirmar Contraseña', widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'}), required=True)

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class LoginUserForm(AuthenticationForm):
    username = CharField(label='Nombre de usuario', required=True, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }
    ))
    class Meta:
        fields = [
            'username',
            'password'
        ]


