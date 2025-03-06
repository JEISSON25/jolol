from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Estudiante
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = EstudianteSerializer
    filterset_fields = ('__all__')  # Reemplaza 'campo1', 'campo2' por los nombres de los campos que deseas filtrar
    search_fields = ('__all__')       # Reemplaza 'campo1', 'campo2' por los campos en los que se realizará la búsqueda
    ordering_fields = ('__all__')     # Si deseas habilitar el ordenamiento
