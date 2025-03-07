from rest_framework import serializers
from .models import Candidato, TipoEleccion, Voto
from apps.archivo.models import Archivo  # Asegúrate de importar el modelo Archivo

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'  # O especifica los campos que necesitas

class TipoEleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEleccion
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'

class CandidatoSerializer(serializers.ModelSerializer):
    eleccion = TipoEleccionSerializer()  # Representación anidada para TipoEleccion
    archivo = ArchivoSerializer()        # Representación anidada para Archivo

    class Meta:
        model = Candidato
        fields = '__all__'
