from django.contrib import admin
from avaliacoes.models import Avaliacao


@admin.register(Avaliacao)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','filme','estrelas','comentario')
