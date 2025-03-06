from django.db import models
from apps.common.models import TimeStampedModel
from apps.empresas.models import Empresa

class Mesa(TimeStampedModel):
    nombre = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
