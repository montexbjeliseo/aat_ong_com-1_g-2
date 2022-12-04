from django.db import models
from apps.usuarios.models import *
# Mi dispiace per le lingue tutte mischiate
# Create your models here.

class Categoria(models.Model):
	name = models.CharField(max_length = 60)
	description = models.CharField(max_length = 250, null = True, blank = True)

	def __str__(self):
		return self.name


class Noticia(models.Model):
	title = models.CharField(max_length = 120)
	created_at = models.DateField(auto_now_add = True)
	body = models.TextField()
	author = models.CharField(max_length = 50, null=True, blank = True)
	image = models.ImageField(upload_to = 'noticias', null=True, blank = True)
	category = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.title

	def get_comentarios(self):
		return self.comentarios.all()

class Comentario(models.Model):
	noticias = models.ForeignKey(Noticia, related_name = 'comentarios', on_delete = models.CASCADE)
	text = models.TextField()
	create_at = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(Usuario, related_name = 'usuarios_comentarios' , on_delete = models.CASCADE)

	def __str__(self):
		return self.text