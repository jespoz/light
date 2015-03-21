from django.db import models
from reports.models import TipoPeriodo

class ZonaVentas(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    zona = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Zona de Ventas'
        verbose_name_plural = 'Zonas de Ventas'

    def __unicode__(self):
        return self.zona

class OficinaVentas(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    oficina = models.CharField(max_length=50)
    zona = models.ForeignKey(ZonaVentas, default='', null=True)

    class Meta:
        verbose_name = 'Oficina de Ventas'
        verbose_name_plural = 'Oficinas de Ventas'

    def __unicode__(self):
        return self.oficina

class Periodo(models.Model):
    tipoPeriodo = models.ForeignKey(TipoPeriodo, default='', null=True)
    periodo = models.CharField(max_length=20)

    def __unicode__(self):
        return self.periodo

class CCNivel1(models.Model):
    clasecoste = models.CharField(max_length=200)

    def __unicode__(self):
        return self.clasecoste

class CCNivel2(models.Model):
    clasecoste = models.CharField(max_length=200)
    nivel1 = models.ForeignKey(CCNivel1)
    seudo = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.clasecoste

class CCNivel3(models.Model):
    clasecoste = models.CharField(max_length=200)
    nivel2 = models.ForeignKey(CCNivel2)
    color = models.CharField(max_length=10, default='', null=True)

    def __unicode__(self):
        return self.clasecoste

class ClasesCoste(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    clasecoste = models.CharField(max_length=200)
    nivel3 = models.ForeignKey(CCNivel3, null=True, default='')
    seudo = models.CharField(max_length=100, null=True, default='')

    def __unicode__(self):
        return '%s %s' % (self.codigo, self.clasecoste4)

class GrupoSector(models.Model):
    grupo = models.CharField(max_length=100)

    def __unicode__(self):
        return self.grupo

class Sector(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    sector = models.CharField(max_length=100)
    id = models.IntegerField(default=0)
    grupo = models.ForeignKey(GrupoSector, null=True, default='')

    class Meta:
        verbose_name_plural = 'Sectores'

    def __unicode__(self):
        return self.sector

class TipoCliente(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    tipo = models.CharField(max_length=100)
    abreviacion = models.CharField(max_length=10, default='')

    class Meta:
        verbose_name = 'Tipo de Cliente'
        verbose_name_plural = 'Tipos de Clientes'

    def __unicode__(self):
        return self.tipo

class Cadena(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    cadena = models.CharField(max_length=100)

    def __unicode__(self):
        return self.cadena

class ClasePedido(models.Model):
    codigo = models.CharField(max_length=200, primary_key=True)
    clase = models.CharField(max_length=200)

    def __unicode__(self):
        return self.clase

class Cliente(models.Model):
    codigo = models.IntegerField(max_length=20, primary_key=True)
    cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100, null=True)
    creacion = models.DateField(null=True)

class CategoriaCliente(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    categoria = models.CharField(max_length=100)

    def __unicode__(self):
        return self.categoria

class ClienteInterlocutor(models.Model):
    cliente = models.IntegerField(max_length=20)
    sector = models.ForeignKey(Sector, null=True, blank=True, default='')
    supervisor = models.CharField(max_length=200, default='', null=True, blank=True)
    preventa = models.CharField(max_length=200, default='', null=True, blank=True)

class LocalesNulos(models.Model):
    cliente = models.IntegerField(max_length=20)