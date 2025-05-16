from django.db import models

# constante para dar opções de itens para selecionar no campo nacionalidade
NAC_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
)


class Ator(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField(blank=True, null=True)
    nacionalidade = models.CharField(
        max_length=100,
        choices=NAC_CHOICES,  # campo choice abre uma lista de opções para selecionar
        blank=True,
        null=True,
    )

    # essa função define qual campo vai ser mostrado na tela
    def __str__(self):
        return self.nome
