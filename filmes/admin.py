from django.contrib import admin
from filmes.models import Filme


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano_lancamento', 'resumo', 'genero',]
    list_filter = ['genero']
    search_fields = ['titulo']
