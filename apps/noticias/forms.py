from django.forms import *
from .models import *
from django.utils.html import strip_tags

class NuevaNoticiaForm(ModelForm):
    titulo = CharField(label='Titulo', required=True, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia'}))
    cuerpo = CharField(label='Cuerpo de la noticia', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Cuerpo de la noticia'
        }))
    imagen = ImageField(label="Imagen", widget=FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Noticia
        exclude = [
            'creado',
            'autor',
            'visitas',
        ]
    def clean_cuerpo(self):
        d_cuerpo = self.cleaned_data['cuerpo']
        if len(strip_tags(d_cuerpo)) < 50:
            raise ValidationError('El mínimo de caracteres es de 50')
        return d_cuerpo

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
    mensaje = CharField(label='Comenta', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'rows': 4,
        'placeholder': 'Mensaje'
        }))
    class Meta:
        model = Contacto
        fields = [
            'nombre', 
            'email',
            'mensaje'
        ]