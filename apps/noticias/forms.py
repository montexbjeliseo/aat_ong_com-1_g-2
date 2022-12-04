from django.forms import *
from .models import *

class NuevaNoticiaForm(ModelForm):
    title = CharField(label='Titulo', required=True, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia'}))
    category = ModelMultipleChoiceField(
                        queryset=Categoria.objects.all().order_by('name'),
                        label="Categoria",
                        widget=CheckboxSelectMultiple)
    body = CharField(label='Cuerpo de la noticia', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Cuerpo de la noticia'
        }))

    class Meta:
        model = Noticia
        exclude = [
            'author',
            'created_at',
            'updated_at',
        ]
    