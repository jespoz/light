from django.contrib.auth.models import User
from django.db import models


class TipoPeriodo(models.Model):
    tipo = models.CharField(max_length=140)

    def __unicode__(self):
        return self.tipo

class Infografia(models.Model):
    infografia = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tipoPeriodo = models.ForeignKey(TipoPeriodo, default='', null=True)

    def __unicode__(self):
        return self.infografia

class Reporte(models.Model):
    infografia = models.ForeignKey(Infografia)
    reporte = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    sap = models.CharField(max_length=200, default='')
    matriz = models.FileField(upload_to='matrices/', null=True, blank=True)
    icono = models.CharField(max_length=100, default='', null=True, blank=True)
    url_django = models.CharField(max_length=100, default='', null=True, blank=True)

    def __unicode__(self):
        return self.reporte