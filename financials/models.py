from django.db import models
from master.models import OficinaVentas, Periodo, ClasesCoste, Sector, TipoCliente, Cadena, CCNivel2, CCNivel3

class Kilos(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente, default='', null=True)
    kilos = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Kilos'

    def __unicode__(self):
        return '%s %s' % (self.oficina, self.periodo)

class Gasto(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    clasecoste = models.ForeignKey(ClasesCoste)
    sector = models.ForeignKey(Sector)
    gasto = models.FloatField(default=0)

class EERR(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    kilo = models.FloatField(default=0, null=True)
    venta = models.FloatField(default=0, null=True)
    ingreso = models.FloatField(default=0, null=True)
    gasto = models.FloatField(default=0, null=True)
    margen_peso = models.FloatField(default=0, null=True)
    margen_porc = models.FloatField(default=0, null=True)

    class Meta:
        verbose_name = 'Estado de Resultado'
        verbose_name_plural = 'Estados de Resultado'

class MargenMensual(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    aa = models.FloatField(default=0)
    ac = models.FloatField(default=0)

    def __unicode__(self):
        return self.periodo__periodo

class Unitario(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    ingreso = models.FloatField(default=0)
    gasto = models.FloatField(default=0)

class PrecioPromedio(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente, default='', null=True)
    sector = models.ForeignKey(Sector)
    kilo = models.FloatField(default=0)
    neto = models.FloatField(default=0)

class PPOficina(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    sector = models.ForeignKey(Sector)
    precio = models.FloatField(default=0)
    variacion = models.FloatField(default=0)

class PPTipoCliente(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    precio = models.FloatField(default=0)
    variacion = models.FloatField(default=0)

class PPTipoClienteSector(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    sector = models.ForeignKey(Sector)
    precio = models.FloatField(default=0)
    variacion = models.FloatField(default=0)

class Descuento(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    cadena = models.ForeignKey(Cadena)
    sector = models.ForeignKey(Sector, null=True)
    rut = models.CharField(max_length=20, default='', null=True)
    tipoPedido = models.CharField(max_length=100, default='', null=True)
    kilo = models.FloatField(default=0)
    base = models.FloatField(default=0)
    especial = models.FloatField(default=0)
    vigente = models.FloatField(default=0)
    pedido = models.FloatField(default=0)
    facturado = models.FloatField(default=0)

class DescuentoTotal(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    descuento = models.FloatField(default=0)
    comercial = models.FloatField(default=0)
    vigente = models.FloatField(default=0)
    sucursal = models.FloatField(default=0)
    participacion = models.FloatField(default=0)

class DescuentoComercial(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    descuento = models.FloatField(default=0)

class DescuentoVigente(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    descuento = models.FloatField(default=0)

class DescuentoSucursal(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    vigente = models.FloatField(default=0)
    pedido = models.FloatField(default=0)
    facturado = models.FloatField(default=0)
    peso_pedido = models.FloatField(default=0)
    peso_facturado = models.FloatField(default=0)

class DescuentoPedido(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    descuento = models.FloatField(default=0)

class DescuentoTCPedido(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    descuento = models.FloatField(default=0)

class DescuentoFacturado(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    descuento = models.FloatField(default=0)

class DescuentoTCFacturado(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    descuento = models.FloatField(default=0)

class Costo(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    claseCoste = models.ForeignKey(CCNivel2)
    costo = models.FloatField(default=0)

class CostoVentas(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    claseCoste = models.ForeignKey(CCNivel3)
    sucursal = models.FloatField(default=0)
    zonal = models.FloatField(default=0)
    nacional = models.FloatField(default=0)

class CostoApertura(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    claseCoste = models.ForeignKey(ClasesCoste)
    costo = models.FloatField(default=0)
    peso = models.FloatField(default=0)

class EstadosResultados(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    kilo = models.FloatField(default=0, null=True)
    venta = models.FloatField(default=0, null=True)
    ingreso = models.FloatField(default=0, null=True)
    gasto = models.FloatField(default=0, null=True)
    margen_peso = models.FloatField(default=0, null=True)
    margen_porc = models.FloatField(default=0, null=True)
    crec_kilo = models.FloatField(default=0, null=True)
    crec_venta = models.FloatField(default=0, null=True)
    crec_ingreso = models.FloatField(default=0, null=True)
    crec_gasto = models.FloatField(default=0, null=True)

class PesoTipoCliente(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    tipoCliente = models.ForeignKey(TipoCliente)
    peso = models.FloatField(default=0)

class PesoDescCallPed(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    total = models.FloatField(default=0)
    call = models.FloatField(default=0)

class PesoDescCallFact(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    total = models.FloatField(default=0)
    call = models.FloatField(default=0)

class CostoTotal(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    sucursal = models.FloatField(default=0)
    zonal = models.FloatField(default=0)
    nacional = models.FloatField(default=0)

class PesoGastoVenta(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    gasto = models.FloatField(default=0)

class CostoDistrSec(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    gasto = models.FloatField(default=0)

class CostoDistrSecAcum(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    sucursal = models.FloatField(default=0)
    zonal = models.FloatField(default=0)
    nacional = models.FloatField(default=0)

class CostoMerchAcum(models.Model):
    oficina = models.ForeignKey(OficinaVentas)
    periodo = models.ForeignKey(Periodo)
    sucursal = models.FloatField(default=0)
    zonal = models.FloatField(default=0)
    nacional = models.FloatField(default=0)

class PesoMateriales(models.Model):
    periodo = models.ForeignKey(Periodo)
    oficina = models.ForeignKey(OficinaVentas)
    material = models.IntegerField()
