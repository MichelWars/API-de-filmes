from rest_framework import serializers

from atores.models import Ator


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator  # aponta qual model sera mostrado
        fields = '__all__'   # aponta quais campos do model seram mostrados
