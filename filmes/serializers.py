from django.db.models import Avg
from rest_framework import serializers

from atores.serializers import ActorSerializer
from filmes.models import Filme
from generos.serializers import GenreSerializer


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

    def validate_ano_lancamento(self, value):   # valiadação de valores
        if value < 1900:
            raise serializers.ValidationError(
                'A data de lançamento não pode ser inferior a 1990!'
            )
        return value

    def validate_resumo(self, value):   # valida quantidade de caracteres
        if len(value) > 500:
            raise serializers.ValidationError('Limite 200 caracteres!!')
        return value


class FilmeListSerializer(serializers.ModelSerializer):
    atores = ActorSerializer(many=True)
    genero = GenreSerializer()
    avaliacoes = serializers.SerializerMethodField(
        read_only=True
    )   # cria um campo calculado na consulta

    class Meta:
        model = Filme
        fields = [
            'id',
            'titulo',
            'genero',
            'atores',
            'ano_lancamento',
            'avaliacoes',
            'resumo',
        ]

    def get_avaliacoes(self, obj):   # cria a logica do campo calculado
        avaliacoes = obj.reviews.aggregate(Avg('estrelas'))[
            'estrelas__avg'
        ]   # captura a quantidade de avaliacoes(estrelas), somas as avaliacoes e calcula a media

        if avaliacoes:
            return round(avaliacoes, 1)

        return None
