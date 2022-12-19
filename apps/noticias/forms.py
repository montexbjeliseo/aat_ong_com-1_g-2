from django.forms import *
from .models import *
from django.utils.html import strip_tags
from django.db import models

class NuevaNoticiaForm(ModelForm):
    titulo = CharField(label='Titulo', required=True, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia'}))
    cuerpo = CharField(label='Cuerpo de la noticia', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Cuerpo de la noticia'
        }))
    imagen = ImageField(label="Imagen", widget=FileInput(attrs={'class': 'form-control'}))
    categoria = ModelChoiceField(queryset=Categoria.objects.all(), required=False, widget=Select(attrs={'onchange': 'javascript:alternar_visibilidad_nueva_categoria();'}))
    nueva_categoria = CharField(required=False, widget=TextInput(attrs={'placeholder': 'Nombre nueva categoria'}))
    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'cuerpo',
            'categoria',
            'imagen'
        ]
    def clean_cuerpo(self):
        d_cuerpo = self.cleaned_data['cuerpo']
        if len(strip_tags(d_cuerpo)) < 50:
            raise ValidationError('El mínimo de caracteres es de 50')
        return d_cuerpo

    def clean_categoria(self):
        d_categoria = self.cleaned_data['categoria']
        d_nueva_categoria = self.data['nueva_categoria']
        if not d_categoria and not d_nueva_categoria:
            raise ValidationError('Categoria es obligatoria')
        elif d_nueva_categoria:
            categoria = Categoria(nombre=d_nueva_categoria)
            categoria.save()
            return categoria
        return d_categoria
class NuevaCategoriaForm(ModelForm):
    nombre = CharField(label='Nombre de la categoria', required=True, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}))
    descripcion = CharField(label='Descripcion', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Descripcion'
        }))
    class Meta:
        model = Categoria
        exclude = [
            'creado'
        ]

class NuevoComentarioForm(ModelForm):
    texto = CharField(label='Comenta', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'rows': 4,
        'placeholder': 'Deja tu comentario'
        }))
    class Meta:
        model = Comentario
        fields = [
            'texto'
        ]


class NuevoContactoForm(ModelForm):
    nombre = CharField(label='Nombre del contacto', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre'}))
    email= CharField(label = 'Correo electrónico', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico'}))
    mensaje = CharField(label='Comenta', required=True, widget=TextInput(attrs={
        'class': 'form-control',
        'rows':4,
        'placeholder': 'Mensaje'}))

    class Meta:
        model = Contacto     
        fields = [
            'nombre',
            'email',
            'mensaje'
        ]
