from rest_framework import serializers
from .models import MiUsuario


class MiUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiUsuario
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
            'fecha_nacimiento',
            'biografia',
        ]
        read_only_fields = ['id']


#El serializador permite convertir informacion de los usuarios a JSON para que pueda utilizarse en nuestra API        