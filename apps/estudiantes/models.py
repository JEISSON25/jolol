from django.db import models
from apps.common.models import TimeStampedModel
from apps.empresas.models import Empresa  # Se usa para relacionar id_empresa

class Estudiante(TimeStampedModel):
    documento = models.CharField(max_length=50, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    qr_sufragante = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    sede = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    votado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
