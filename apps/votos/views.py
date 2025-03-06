from rest_framework import viewsets
from .models import Voto
from .serializers import VotoSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer
