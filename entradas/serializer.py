
from rest_framework import serializers
from .models import Categoria, Estado, Entrada, HistorialEstado


# Convertir los modelos a JSON para ser consumidos por el frontend


# Serializer de categorías
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


# Serializer de estados
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


# Serializer de entradas del diario personal
class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'
        read_only_fields = ['usuario']


# Serializer del historial de estados
class HistorialEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstado
        fields = '__all__'
