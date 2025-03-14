from rest_framework import viewsets
from .models import *
from .serializers import *

class PuestoVotacionViewSet(viewsets.ModelViewSet):
    queryset = PuestoVotacion.objects.all()
    serializer_class = PuestoVotacionSerializer


class DetailPuestoVotacionViewSet(viewsets.ModelViewSet):
    queryset = DetailPuestoVotacion.objects.all()
    serializer_class = DetailPuestoVotacionSerializer