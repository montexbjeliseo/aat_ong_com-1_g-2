from django.forms import *
from .models import *

class NuevoSlideFormulario(ModelForm):
    texto = CharField(label='Texto de presentación', required=True, widget=Textarea(attrs={
        'class': 'form-control', 
        'rows': 4,
        'placeholder': 'Texto de presentación'
        }))
    class Meta:
        model = Slide
        fields = [
            'texto',
            'imagen',
        ]