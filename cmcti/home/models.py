from django.db import models
from register.models import CustomUser

# Create your models here.
TIPOS = (
    ('Demanda','Demanda'),
    ('Documento','Documento')
    )
    


class Demanda(models.Model):
    titulo = models.CharField(max_length=300, blank=False, null=False)
    tipo = models.CharField(choices=TIPOS, blank=False, null=False, max_length=50)
    descricao = models.TextField(blank=False, null=False)
    prazo = models.DateField(blank=True)
    documento = models.FileField(blank=True, upload_to='documentos/', null=True)
    criado_por = models.ManyToManyField(CustomUser)
    concluida = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.titulo