from django.db import models
from master.models import OficinaVentas, Periodo
from reports.models import Reporte


class MensajeReporte(models.Model):
    reporte = models.ForeignKey(Reporte)
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    primera = models.IntegerField(default=0, null=True)
    segunda = models.IntegerField(default=0, null=True)
    tercera = models.IntegerField(default=0, null=True)

    def __unicode__(self):
        return "%s %s" % (self.reporte, self.periodo)

class MensajesAleatorios(models.Model):
    reporte = models.ForeignKey(Reporte)
    tipo = models.IntegerField(default=0)
    primera_titulo = models.CharField(max_length=30)
    primera_mensaje = models.TextField()
    segunda_titulo = models.CharField(max_length=30)
    segunda_mensaje = models.TextField()
    tercera_titulo = models.CharField(max_length=30)
    tercera_mensaje = models.TextField()

    def __unicode__(self):
        return "%s del tipo %s con el titulo %s" % (self.reporte, self.tipo, self.primera_titulo)

class Hashtag(models.Model):
    reporte = models.ForeignKey(Reporte)
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    hash = models.CharField(max_length=100)
    valor = models.TextField()
