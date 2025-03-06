from rest_framework import viewsets
from .models import Archivo
from .serializers import ArchivoSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
