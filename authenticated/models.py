from django.db import models
from django.contrib.auth.models import User
from reports.models import Reporte


class Canal(models.Model):
    canal = models.CharField(max_length=50)
    icono = models.ImageField(upload_to='/iconos/', blank=True)

    class Meta:
        verbose_name_plural = 'Canales'

    def __unicode__(self):
        return self.canal

class Cadena(models.Model):
    cadena = models.CharField(max_length=50)
    icono = models.ImageField(upload_to='/iconos/', blank=True)

    def __unicode__(self):
        return self.cadena

class Oficina(models.Model):
    codigo = models.CharField(max_length=4)
    oficina = models.CharField(max_length=50)

    def __unicode__(self):
        return self.oficina

class Cargo(models.Model):
    cargo = models.CharField(max_length=50)

    def __unicode__(self):
        return self.cargo

class Perfil(models.Model):
    cargo = models.ForeignKey(Cargo, default='')
    usuario = models.ForeignKey(User)
    canal = models.ManyToManyField(Canal)
    cadena = models.ManyToManyField(Cadena)
    oficina = models.ManyToManyField(Oficina)

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __unicode__(self):
        return self.usuario.username

class AccesoReporte(models.Model):
    cargo = models.ForeignKey(Cargo)
    reporte = models.ManyToManyField(Reporte)

    def __unicode__(self):
        return self.cargo.cargo

class Prioridad(models.Model):
    usuario = models.ForeignKey(User)
    reporte = models.ForeignKey(Reporte)
    ingresos = models.IntegerField(default=0)
    promedio = models.FloatField(default=0)