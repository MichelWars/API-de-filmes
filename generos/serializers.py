from rest_framework import serializers
from generos.models import Genero


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
