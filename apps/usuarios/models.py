from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	imagen=models.ImageField(upload_to="usuarios",null=True,blank=True)