from django.contrib import admin
from .models import *

@admin.register(OficinaVentas)
class OficinaVentasAdmin(admin.ModelAdmin):
    pass

@admin.register(ZonaVentas)
class ZonaVentasAdmin(admin.ModelAdmin):
    pass

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    pass

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Cadena)
class CadenaAdmin(admin.ModelAdmin):
    pass
