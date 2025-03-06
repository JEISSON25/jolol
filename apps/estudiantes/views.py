from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Estudiante
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'  # Permite filtrar por todos los campos del modelo
    search_fields = '__all__'     # Permite buscar en todos los campos (si es compatible con tu configuración)
    ordering_fields = '__all__'   # O bien, lista explícitamente los campos, por ejemplo: ['campo1', 'campo2']
