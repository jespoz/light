from django.db import models
from master.models import Periodo, OficinaVentas, TipoCliente, Sector, CategoriaCliente, GrupoSector

class FormulaDeIngreso(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    cliente = models.IntegerField(max_length=20)
    tipoCliente = models.ForeignKey(TipoCliente, default='', null=True)
    sector = models.ForeignKey(Sector, default='', null=True)
    categoria = models.ForeignKey(CategoriaCliente, default='', null=True)
    fecha = models.DateField()
    supervisor = models.CharField(max_length=200, default='', null=True, blank=True)
    preventa = models.CharField(max_length=200, default='', null=True, blank=True)
    kilo = models.FloatField()
    neto = models.FloatField()

class FI_Totales(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    kilo = models.FloatField()
    var_kilo = models.FloatField(default=0)
    neto = models.FloatField()
    var_neto = models.FloatField(default=0)
    precio = models.FloatField()
    locales = models.FloatField()
    frecuencia = models.FloatField()
    ticket = models.FloatField()

class FI_Comparativo(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    sem_precio = models.FloatField()
    sem_local = models.FloatField()
    sem_frecuencia = models.FloatField()
    sem_ticket = models.FloatField()
    mes_precio = models.FloatField(default=0)
    mes_local = models.FloatField(default=0)
    mes_frecuencia = models.FloatField(default=0)
    mes_ticket = models.FloatField(default=0)

class FI_MesAnterior(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    precio = models.FloatField()
    local = models.FloatField()
    frecuencia = models.FloatField()
    ticket = models.FloatField()

class FI_MesCurso(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    precio = models.FloatField()
    local = models.FloatField()
    frecuencia = models.FloatField()
    ticket = models.FloatField()

class FI_DetallePrecio(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    sector = models.ForeignKey(Sector)
    sucursal = models.FloatField(default=0)
    zonal = models.FloatField(default=0)
    nacional = models.FloatField(default=0)

class FI_LocalesNuevos(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    locales = models.IntegerField(default=0)

class FI_Locales(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    locales = models.IntegerField(default=0)

class FI_LocalesRecuperados(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    locales = models.IntegerField(default=0)

class FI_LocalesFugados(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    locales = models.IntegerField(default=0)

class IconosLocales(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    fa_locales = models.IntegerField(default=0)
    fa_nuevos = models.IntegerField(default=0)
    fa_recuperados = models.IntegerField(default=0)

class FI_DetalleFrecuencia(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    categoria = models.ForeignKey(CategoriaCliente)
    crudo = models.FloatField(default=0)
    procesado = models.FloatField(default=0)

class FI_DetalleTicket(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    dia = models.CharField(max_length=2)
    crudo = models.FloatField(default=0)
    procesado = models.FloatField(default=0)
