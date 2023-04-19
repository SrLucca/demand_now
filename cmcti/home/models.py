from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Demanda(models.Model):
    titulo = models.CharField(max_length=300, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    prazo = models.DateField(blank=True)
    criado_por = models.ManyToManyField(User)

    def __str__(self):
        return self.titulo