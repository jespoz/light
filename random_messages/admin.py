from django.contrib import admin
from random_messages.models import MensajesAleatorios, MensajeReporte


@admin.register(MensajeReporte)
class MensajesAleatoriosAdmin(admin.ModelAdmin):
    pass

@admin.register(MensajesAleatorios)
class MensajesAleatoriosAdmin(admin.ModelAdmin):
    pass
