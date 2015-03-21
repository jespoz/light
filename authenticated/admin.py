from django.contrib import admin
from .models import Cadena, Canal, Oficina, Perfil, Cargo, AccesoReporte

@admin.register(Cadena)
class CadenaAdmin(admin.ModelAdmin):
    pass

@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    pass

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    pass

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    filter_horizontal = ('canal','cadena', 'oficina',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass

@admin.register(AccesoReporte)
class AccesoReporteAdmin(admin.ModelAdmin):
    filter_horizontal = ('reporte',)