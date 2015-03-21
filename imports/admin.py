from django.contrib import admin
from .models import file

@admin.register(file)
class fileAdmin(admin.ModelAdmin):
    pass
