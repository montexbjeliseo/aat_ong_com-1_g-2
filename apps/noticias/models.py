from django.db import models
from apps.usuarios.models import *
from django.urls import reverse_lazy
from django.utils.html import strip_tags

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)
	def __str__(self):
		return self.nombre
	def get_absolute_url(self):
		return reverse_lazy('noticias:index') + "?categoria="+str(self.pk)

class Noticia(models.Model):
	titulo = models.CharField(max_length = 120)
	creado = models.DateTimeField(auto_now_add = True)
	cuerpo = models.TextField()
	autor = models.ForeignKey(Usuario, models.SET_NULL, null = True)
	imagen = models.ImageField(upload_to = 'noticias', null=True, blank = True)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True)
	visitas = models.IntegerField(default=0)
	likes = models.ManyToManyField(Usuario, blank=True, related_name='likes_noticias')
	
	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse_lazy('noticias:ver', args=[self.pk])

	def get_link_comentar(self):
		return reverse_lazy('noticias:comentar', args=[self.pk])

	def get_link_editar(self):
		return reverse_lazy('noticias:editar', args=[self.pk])
		
	def get_resumen(self):
		texto = strip_tags(self.cuerpo)
		if len(texto) >= 50:
			return texto[0:47] + "..."
		return texto

	def get_cantidad_likes(self):
		return len(self.likes.all())

	def get_cantidad_comentarios(self):
		return len(self.comentario_set.all())

	def get_link_like(self):
		return reverse_lazy('noticias:megusta', args=[self.pk])

class Comentario(models.Model):
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	texto = models.TextField(max_length=1000, help_text="Deja un comentario")
	creado = models.DateTimeField(auto_now_add = True)
	modificado = models.DateTimeField(auto_now_add = True)
	editado = models.BooleanField(default = False)
	usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL, null = True)
	likes = models.ManyToManyField(Usuario, blank=True, related_name='likes_comentarios')
	
	class Meta:
		ordering = ["creado"]

	def __str__(self):
		return self.texto

	def get_link_editar(self):
		return reverse_lazy('noticias:editar_comentario', args=[self.noticia.pk, self.pk])
	
	def get_link_like(self):
		return reverse_lazy('noticias:megusta_comentario', args=[self.noticia.pk, self.pk])
	
	def get_cantidad_likes(self):
		return len(self.likes.all())