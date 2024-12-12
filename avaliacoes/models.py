from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from filmes.models import Filme


class Avaliacao(models.Model):
    filme = models.ForeignKey(
        Filme,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    estrelas = models.IntegerField(
        validators=[
            MinValueValidator(0,'Minimo 0 estrelas'),
            MaxValueValidator(5,'Maximo 5 estrelas'),
        ]
    )
    comentario = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.filme.titulo