from django.db import models
from apps.common.models import TimeStampedModel
from apps.empresas.models import Empresa

class Mesa(TimeStampedModel):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
