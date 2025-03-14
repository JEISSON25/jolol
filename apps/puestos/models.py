from django.db import models
from apps.common.models import TimeStampedModel
from apps.mesas.models import Mesa
from apps.empresas.models import Empresa


class PuestoVotacion(models.Model):
    nombre = models.CharField(max_length=100)
    state = models.BooleanField("Estado", default=False)
    sincro = models.BooleanField("Sincronizada", default=False)
    config = models.BooleanField("Configurado", default=False)

    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE, 
        related_name='empresa'
    )

    def __str__(self):
        return self.nombre


class DetailPuestoVotacion(models.Model):
    puesto = models.ForeignKey(
        PuestoVotacion, 
        on_delete=models.CASCADE, 
        related_name='puesto_votacion'
    )
    mesa = models.ForeignKey(
        Mesa, 
        on_delete=models.CASCADE, 
        related_name='mesa'
    )

    def __str__(self):
        return f'{self.mesa}'