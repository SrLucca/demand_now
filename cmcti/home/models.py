from django.db import models
from register.models import CustomUser

# Create your models here.

class Demanda(models.Model):
    titulo = models.CharField(max_length=300, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    prazo = models.DateField(blank=True)
    documento = models.FileField(blank=True, upload_to='documentos')
    criado_por = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.titulo