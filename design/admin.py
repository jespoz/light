from django.contrib import admin
from design.models import Navegacion, Acceso


@admin.register(Navegacion)
class NavegacionAdmin(admin.ModelAdmin):
    pass

@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    filter_horizontal = ('navegacion',)

