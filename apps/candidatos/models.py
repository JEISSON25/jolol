from django.db import models
from apps.common.models import TimeStampedModel
from apps.empresas.models import Empresa
from apps.archivo.models import Archivo
from apps.votos.models import Voto
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from django.db import models

class TipoEleccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Candidato(TimeStampedModel):
    nombre = models.CharField(max_length=100)
    archivo = models.ForeignKey(Archivo, null=True, blank=True, on_delete=models.SET_NULL, related_name='candidatos')
    eleccion = models.ForeignKey(
        TipoEleccion, 
        on_delete=models.CASCADE, 
        related_name='candidatos'
    )
    tarjeton = models.IntegerField("Tarjeton", blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    votos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


@receiver(post_save, sender=Voto)
def set_voto(sender, instance, created, **kwargs):

    if created:
        instance.candidato.votos += 1
        instance.candidato.save()