from django.forms import *
from .models import *

class NuevaNoticiaForm(ModelForm):
    titulo = CharField(label='Titulo', required=True, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia'}))
    """category = ModelMultipleChoiceField(
                        queryset=Categoria.objects.all().order_by('name'),
                        label="Categoria",
                        widget=CheckboxSelectMultiple)"""
    cuerpo = CharField(label='Cuerpo de la noticia', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Cuerpo de la noticia'
        }))

    class Meta:
        model = Noticia
        exclude = [
            'creado',
            'autor',
            'categoria'
        ]

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