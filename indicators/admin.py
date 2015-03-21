from django.contrib import admin
from .models import Indicador, Visualizacion

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    pass

@admin.register(Visualizacion)
class VisualizacionAdmin(admin.ModelAdmin):
    pass
