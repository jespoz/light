from django.contrib import admin
from .models import Kilos, EERR

@admin.register(Kilos)
class KilosAdmin(admin.ModelAdmin):
    pass

@admin.register(EERR)
class EERRAdmin(admin.ModelAdmin):
    pass
