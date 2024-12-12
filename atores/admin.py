from django.contrib import admin
from .models import Ator

@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_filter = ('nacionalidade',)
    search_fields = ('nome',)


