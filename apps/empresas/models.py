from django.db import models
from apps.common.models import TimeStampedModel
from apps.archivo.models import Archivo


class Empresa(TimeStampedModel):
    nombre = models.CharField(max_length=100)
    archivo = models.ForeignKey(Archivo, null=True, blank=True, on_delete=models.SET_NULL, related_name='empresas')
    state = models.BooleanField("En vivo", default=False)
    public = models.BooleanField("Publico", default=False)

    def __str__(self):
        return self.nombre
