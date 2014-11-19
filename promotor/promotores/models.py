from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Pessoa(AbstractUser):
	descricao = models.CharField(max_length=100, blank=True, null=True)
	endereco = models.CharField(max_length=100, blank=True, null=True)