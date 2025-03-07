from rest_framework import serializers
from .models import Candidato, TipoEleccion

class TipoEleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEleccion
        fields = '__all__'

class CandidatoSerializer(serializers.ModelSerializer):
    eleccion = TipoEleccionSerializer()  # Representación anidada

    class Meta:
        model = Candidato
        fields = '__all__'
