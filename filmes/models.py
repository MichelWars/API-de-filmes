from django.db import models
from generos.models import Genero
from atores.models import Ator


class Filme(models.Model):
    titulo = models.CharField(max_length=500)
    genero = models.ForeignKey(
        Genero,
        on_delete=models.PROTECT, # chave estrangeira protegida contra exclusão acidental
        related_name='filmes' # nome do relacionamento
    )
    ano_lancamento = models.IntegerField(blank=True, null=True)
    atores = models.ManyToManyField(Ator, related_name='filmes')
    resumo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
