from django.db import models
from apps.common.models import TimeStampedModel
from apps.estudiantes.models import Estudiante
from apps.candidatos.models import Candidato
from apps.mesas.models import Mesa
from apps.empresas.models import Empresa

class Voto(TimeStampedModel):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    candidato1 = models.ForeignKey(Candidato, related_name='votos_candidato1', on_delete=models.CASCADE)
    candidato2 = models.ForeignKey(Candidato, related_name='votos_candidato2', on_delete=models.CASCADE)
    fechaHora = models.DateTimeField(auto_now_add=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Voto de {self.estudiante}"
