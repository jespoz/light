from django.contrib.auth.models import User
from django.db import models
from authenticated.models import Cargo
from master.models import OficinaVentas
from master.models import Periodo
from reports.models import Reporte


class DatosTimeline(models.Model):
    reporte = models.ForeignKey(Reporte)
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    resultado = models.FloatField(default=0)

class Navegacion(models.Model):
    nav = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nav

class ControlIngreso(models.Model):
    usuario = models.ForeignKey(User)
    reporte = models.ForeignKey(Reporte)
    ingreso = models.DateTimeField()
    salida = models.DateTimeField(null=True)

class Acceso(models.Model):
    cargo = models.ForeignKey(Cargo)
    navegacion = models.ManyToManyField(Navegacion)

class Chat(models.Model):
    autor = models.CharField(max_length=150)
    comentario = models.TextField()

    def __unicode__(self):
        return self.autor
