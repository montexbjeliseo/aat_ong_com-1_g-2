from django.db import models
from apps.usuarios.models import *

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)
	descripcion = models.CharField(max_length = 250, null = True, blank = True)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):
	titulo = models.CharField(max_length = 120)
	creado = models.DateField(auto_now_add = True)
	cuerpo = models.TextField()
	autor = models.ForeignKey(Usuario, models.SET_NULL, null = True)
	imagen = models.ImageField(upload_to = 'noticias', null=True, blank = True)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True)

	class Meta:
		ordering = ["-creado"]

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	texto = models.TextField(max_length=1000, help_text="Deja un comentario")
	creado = models.DateTimeField(auto_now_add = True)
	usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL, null = True)
	
	class Meta:
		ordering = ["creado"]

	def __str__(self):
		return self.texto