from rest_framework import serializers
from .models import *
from ..mesas.serializers import *


class PuestoVotacionSerializer(serializers.ModelSerializer):
    # archivo = ArchivoSerializer()        

    class Meta:
        model = PuestoVotacion
        fields = '__all__'


class DetailPuestoVotacionSerializer(serializers.ModelSerializer):
    mesa = MesaSerializer()        

    class Meta:
        model = DetailPuestoVotacion
        fields = '__all__'
