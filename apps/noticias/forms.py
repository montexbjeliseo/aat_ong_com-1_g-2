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