from django.db import models

# Create your models here.

class Slide(models.Model):
    texto = models.CharField(max_length = 250, null = True, blank = True)
    imagen = models.ImageField(upload_to = 'slides', null=True, blank = True)
    creado = models.DateField(auto_now_add = True)
