from django.db import models
from master.models import Periodo, OficinaVentas, TipoCliente, Sector


class VentaSumatoriaMaterial(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    tipoCliente = models.ForeignKey(TipoCliente)
    codigoMaterial = models.IntegerField()
    neto = models.FloatField(default=0)
    sumatoria = models.FloatField(default=0)

class VentaAccPrecioTotal(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    sector = models.ForeignKey(Sector)
    referencia = models.IntegerField(default=0)
    unidad = models.FloatField(default=0)
    codigoMaterial = models.IntegerField()
    material = models.CharField(max_length=100)

class BaseAccPrecioTotal(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    sector = models.ForeignKey(Sector)
    referencia = models.IntegerField(default=0)
    unidad = models.FloatField(default=0)
    codigoMaterial = models.IntegerField()
    material = models.CharField(max_length=100)
    diferencia = models.FloatField(default=0)
    observacion = models.CharField(max_length=100)
