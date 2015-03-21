from django.contrib.auth.models import User
from django.db import models
from time import time
from master.models import Periodo, OficinaVentas, TipoCliente, CategoriaCliente, Sector
from reports.models import Reporte


def get_upload_file_name(instance, filename):
    return 'imports/%s_%s' % (str(time()).replace('.', '_'), filename)

class file(models.Model):
    archivo = models.FileField(upload_to=get_upload_file_name, blank=False)

class HistorialCreacionReporte(models.Model):
    usuario = models.ForeignKey(User)
    actualizacion = models.DateTimeField()
    periodo = models.ForeignKey(Periodo)
    reporte = models.ForeignKey(Reporte)

class Timeline(models.Model):
    usuario = models.ForeignKey(User, related_name='usuario_lector')
    reporte = models.ForeignKey(Reporte)
    actualizacion = models.DateTimeField()
    periodo = models.ForeignKey(Periodo)
    creado_por = models.ForeignKey(User, related_name='creador')

class VentaCompleta(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    tipoCliente = models.ForeignKey(TipoCliente)
    categoria = models.ForeignKey(CategoriaCliente)
    sector = models.ForeignKey(Sector)
    cliente = models.IntegerField(max_length=20)
    fecha = models.DateField()
    supervisor = models.CharField(max_length=200, default='', null=True, blank=True)
    preventa = models.CharField(max_length=200, default='', null=True, blank=True)
    codigoMaterial = models.IntegerField()
    material = models.CharField(max_length=100)
    nivel2 = models.CharField(max_length=100)
    nivel3 = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    kilo = models.FloatField(default=0)
    neto = models.FloatField(default=0)
    unidad = models.FloatField(default=0)
    periodo = models.ForeignKey(Periodo, default='')
    referencia = models.IntegerField(default=0)

class Factura(models.Model):
    periodo = models.ForeignKey(Periodo)
    referencia = models.IntegerField(default=0)
    codigoMaterial = models.IntegerField()
    vigente = models.FloatField(default=0)
    pedido = models.FloatField(default=0)
    facturado = models.FloatField(default=0)
