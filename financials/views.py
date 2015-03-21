import json
import random
import cx_Oracle
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView
from design.models import ControlIngreso
from light import settings
from .models import *
from authenticated.models import Perfil
from master.models import OficinaVentas
from random_messages.models import MensajeReporte, MensajesAleatorios, Hashtag
from reports.models import Infografia

class EstadoResultado(TemplateView):
    template_name = 'infographic/eerr.html'

    def get_context_data(self, **kwargs):
        context = super(EstadoResultado, self).get_context_data(**kwargs)
        save_ingreso(self.request.user, 1)
        context['periodo'] = EERR.objects.values('periodo__periodo', 'periodo__id').order_by('-periodo_id')[:1]
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        context['informacion'] = Infografia.objects.all().filter(id=1)
        periodo = ''
        resultado = ''
        costo_to = 0
        costo_ap = 0
        costo_ds = 0
        costo_me = 0
        mano_obra = 0
        validaciones = []
        for per in context['periodo']:
            periodo = per['periodo__periodo']
            periodo_id = per['periodo__id']
        for ofi in context['perfil']:
            for of in ofi.oficina.all():
                periodo_anterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id - 1)
                for pa in periodo_anterior:
                    context['periodo_anterior'] = pa['periodo__id']
                periodo_posterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id + 1)
                for pa in periodo_posterior:
                    context['periodo_posterior'] = pa['periodo__id']
                resultado = EstadosResultados.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['zona'] = OficinaVentas.objects.values('zona__zona').filter(oficina=of.oficina)
                context['real'] = PPOficina.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('sector__id')
                context['pptipocliente'] = PPTipoCliente.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                if context['pptipocliente'].count() > 0:
                    context['ancho_pp_tc'] = (100 / context['pptipocliente'].count()) - 2
                else:
                    context['ancho_pp_tc'] = 0
                context['pptcs'] = PPTipoClienteSector.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo', 'sector__id')
                context['desc_total'] = DescuentoTotal.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['desc_com'] = DescuentoComercial.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['desc_vig'] = DescuentoVigente.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['desc_suc'] = DescuentoSucursal.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['tipoMas'] = DescuentoFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)[:1]
                context['desc_tipo'] = DescuentoFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['desc_sup'] = DescuentoFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(tipoCliente=20)
                context['costos'] = Costo.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('id')
                context['costo_total'] = CostoTotal.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['peso_gasto_venta'] = PesoGastoVenta.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['costo_distr_sec'] = CostoDistrSec.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['costos_ventas'] = CostoVentas.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['costos_aporte'] = CostoApertura.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(claseCoste__nivel3__id=14).order_by('costo')
                context['costos_secundaria'] = CostoApertura.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(claseCoste__nivel3__id=24).order_by('costo')
                context['costos_merchandising'] = CostoApertura.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(claseCoste__nivel3__id=20).order_by('costo')
                context['desc_tc_pedido'] = DescuentoTCPedido.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['desc_tc_facturado'] = DescuentoTCFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['peso_call_ped'] = PesoDescCallPed.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['peso_call_fact'] = PesoDescCallFact.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['mensajePrecioPromedio'] = MensajeReporte.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                for mpp in context['mensajePrecioPromedio']:
                    if(mpp.primera == 0 or mpp.primera == 1):
                        valor = ''.join(['primera', str(mpp.primera)])
                        validaciones.append(valor)
                    if(mpp.segunda == 0 or mpp.segunda == 1):
                        valor = ''.join(['segunda', str(mpp.segunda)])
                        validaciones.append(valor)
                    if(mpp.tercera == 0 or mpp.tercera == 1):
                        valor = ''.join(['tercera', str(mpp.tercera)])
                        validaciones.append(valor)
                if validaciones:
                    seleccion = random.choice(validaciones)
                    context['mensaje'] = MensajesAleatorios.objects.values(''.join([seleccion[:-1], '_titulo']), ''.join([seleccion[:-1], '_mensaje'])).filter(reporte__id=3).filter(tipo=seleccion[-1:])
        for res in resultado:
            context['venta'] = res.venta
            context['venta_crec'] = res.crec_venta
            context['kilo'] = res.kilo
            context['kilo_crec'] = res.crec_kilo
            context['ingreso'] = res.ingreso
            context['ingreso_crec'] = res.crec_ingreso
            context['gasto'] = res.gasto
            context['gasto_crec'] = res.crec_gasto
            context['margen_porc'] = res.margen_porc
            context['margen_peso'] = res.margen_peso
        for desc in context['desc_total']:
            context['peso_desc'] = (desc.sucursal / desc.descuento) * 100
        for tm in context['tipoMas']:
            tipSup = tm.descuento
            context['pesoMas'] = (tipSup / desc.sucursal) * 100
        for costo in context['costos']:
            if (costo.claseCoste.id == 99) or (costo.claseCoste.id == 1):
                mano_obra += costo.costo
        for cost in context['costo_total']:
            costo_to = round((cost.nacional + cost.zonal + cost.sucursal) / 3, 0) + 5
            context['nacional'] = str(round((cost.nacional / costo_to) * 100, 2)).replace(',', '.')
            context['zonal'] = str(round((cost.zonal / costo_to) * 100, 2)).replace(',', '.')
            context['sucursal'] = str(round((cost.sucursal / costo_to) * 100, 2)).replace(',', '.')
        for cost_ap in context['costos_aporte']:
            costo_ap += cost_ap.costo
        for cost_distr in context['costos_secundaria']:
            costo_ds += cost_distr.costo
        for cost_mercha in context['costos_merchandising']:
            costo_me += cost_mercha.costo
        context['total_aporte'] = costo_ap
        context['total_secundaria'] = costo_ds
        context['total_merchandising'] = costo_me
        context['redondeado'] = costo_to
        context['mano_obra'] = mano_obra
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EstadoResultado, self).dispatch(*args, **kwargs)

class EstadoResultadoFiltro(DetailView):
    template_name = 'infographic/eerr.html'
    model = Periodo

    def get_context_data(self, **kwargs):
        context = super(EstadoResultadoFiltro, self).get_context_data(**kwargs)
        save_ingreso(self.request.user, 1)
        context['periodo'] = EERR.objects.values('periodo__periodo', 'periodo__id').filter(periodo__id=self.get_object().pk)[:1]
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        context['informacion'] = Infografia.objects.all().filter(id=1)
        periodo = ''
        resultado = ''
        costo_to = 0
        costo_ap = 0
        costo_ds = 0
        costo_me = 0
        mano_obra = 0
        validaciones = []
        for per in context['periodo']:
            periodo = per['periodo__periodo']
            periodo_id = per['periodo__id']
        for ofi in context['perfil']:
            for of in ofi.oficina.all():
                periodo_anterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id - 1)
                for pa in periodo_anterior:
                    context['periodo_anterior'] = pa['periodo__id']
                periodo_posterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id + 1)
                for pa in periodo_posterior:
                    context['periodo_posterior'] = pa['periodo__id']
                resultado = EstadosResultados.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['zona'] = OficinaVentas.objects.values('zona__zona').filter(oficina=of.oficina)
                context['real'] = PPOficina.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('sector__id')
                context['pptipocliente'] = PPTipoCliente.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['ancho_pp_tc'] = (100 / context['pptipocliente'].count()) - 2
                context['pptcs'] = PPTipoClienteSector.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo', 'sector__id')
                context['desc_total'] = DescuentoTotal.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['desc_com'] = DescuentoComercial.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['desc_vig'] = DescuentoVigente.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['desc_suc'] = DescuentoSucursal.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['tipoMas'] = DescuentoFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)[:1]
                context['desc_tipo'] = DescuentoFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['desc_sup'] = DescuentoFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(tipoCliente=20)
                context['costos'] = Costo.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('id')
                context['costo_total'] = CostoTotal.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['costo_distr_sec'] = CostoDistrSec.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['peso_gasto_venta'] = PesoGastoVenta.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['costos_ventas'] = CostoVentas.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['costos_aporte'] = CostoApertura.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(claseCoste__nivel3__id=14).order_by('costo')
                context['costos_secundaria'] = CostoApertura.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(claseCoste__nivel3__id=24).order_by('costo')
                context['costos_merchandising'] = CostoApertura.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(claseCoste__nivel3__id=20).order_by('costo')
                context['desc_tc_pedido'] = DescuentoTCPedido.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['desc_tc_facturado'] = DescuentoTCFacturado.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('tipoCliente__codigo')
                context['peso_call_ped'] = PesoDescCallPed.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['peso_call_fact'] = PesoDescCallFact.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['mensajePrecioPromedio'] = MensajeReporte.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                for mpp in context['mensajePrecioPromedio']:
                    if(mpp.primera == 0 or mpp.primera == 1):
                        valor = ''.join(['primera', str(mpp.primera)])
                        validaciones.append(valor)
                    if(mpp.segunda == 0 or mpp.segunda == 1):
                        valor = ''.join(['segunda', str(mpp.segunda)])
                        validaciones.append(valor)
                    if(mpp.tercera == 0 or mpp.tercera == 1):
                        valor = ''.join(['tercera', str(mpp.tercera)])
                        validaciones.append(valor)
                seleccion = random.choice(validaciones)
                context['mensaje'] = MensajesAleatorios.objects.values(''.join([seleccion[:-1], '_titulo']), ''.join([seleccion[:-1], '_mensaje'])).filter(reporte__id=2).filter(tipo=seleccion[-1:])
        for res in resultado:
            context['venta'] = res.venta
            context['venta_crec'] = res.crec_venta
            context['kilo'] = res.kilo
            context['kilo_crec'] = res.crec_kilo
            context['ingreso'] = res.ingreso
            context['ingreso_crec'] = res.crec_ingreso
            context['gasto'] = res.gasto
            context['gasto_crec'] = res.crec_gasto
            context['margen_porc'] = res.margen_porc
            context['margen_peso'] = res.margen_peso
        for desc in context['desc_total']:
            context['peso_desc'] = (desc.sucursal / desc.descuento) * 100
        for tm in context['tipoMas']:
            tipSup = tm.descuento
            context['pesoMas'] = (tipSup / desc.sucursal) * 100
        for costo in context['costos']:
            if (costo.claseCoste.id == 99) or (costo.claseCoste.id == 1):
                mano_obra += costo.costo
        for cost in context['costo_total']:
            costo_to = round((cost.nacional + cost.zonal + cost.sucursal) / 3, 0) + 5
            context['nacional'] = str(round((cost.nacional / costo_to) * 100, 2)).replace(',', '.')
            context['zonal'] = str(round((cost.zonal / costo_to) * 100, 2)).replace(',', '.')
            context['sucursal'] = str(round((cost.sucursal / costo_to) * 100, 2)).replace(',', '.')
        for cost_ap in context['costos_aporte']:
            costo_ap += cost_ap.costo
        for cost_distr in context['costos_secundaria']:
            costo_ds += cost_distr.costo
        for cost_mercha in context['costos_merchandising']:
            costo_me += cost_mercha.costo
        context['total_aporte'] = costo_ap
        context['total_secundaria'] = costo_ds
        context['total_merchandising'] = costo_me
        context['redondeado'] = costo_to
        context['mano_obra'] = mano_obra
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EstadoResultadoFiltro, self).dispatch(*args, **kwargs)

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def carga_margen_acumulado(request):
    if request.is_ajax():
        periodo = EERR.objects.values('periodo__id').order_by('-periodo_id')[:1]
        for p in periodo:
            per = p['periodo__id']
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for ofi in perfil:
            for of in ofi.oficina.all():
                meses_json = MargenMensual.objects.values('periodo__periodo', 'periodo__id').filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id')
                meses_dict = ValuesQuerySetToDict(meses_json)
                ciclo_json = serializers.serialize('json', MargenMensual.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                ciclo_list = json.loads(ciclo_json)
                unitario_json = serializers.serialize('json', Unitario.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                unitario_list = json.loads(unitario_json)
                costo_json = serializers.serialize('json', CostoTotal.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                costo_list = json.loads(costo_json)
                distr_json = serializers.serialize('json', CostoDistrSecAcum.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                distr_list = json.loads(distr_json)
                merch_json = serializers.serialize('json', CostoMerchAcum.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                merch_list = json.loads(merch_json)
                json_data = json.dumps({'meses': meses_dict, 'ciclo': ciclo_list, 'unitario': unitario_list, 'costo': costo_list, 'distr_sec': distr_list, 'merchandising': merch_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def carga_costo_venta(request):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').order_by('-periodo_id')[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                costo_json = CostoVentas.objects.values('claseCoste__clasecoste', 'costo', 'claseCoste__color').filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                costo_dict = ValuesQuerySetToDict(costo_json)
                json_data = json.dumps({'costo': costo_dict})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
            raise Http404

def carga_margen_acumulado_filtro(request, pk):
    if request.is_ajax():
        periodo = EERR.objects.values('periodo__id').filter(periodo__id=pk)[:1]
        for p in periodo:
            per = p['periodo__id']
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for ofi in perfil:
            for of in ofi.oficina.all():
                meses_json = MargenMensual.objects.values('periodo__periodo', 'periodo__id').filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id')
                meses_dict = ValuesQuerySetToDict(meses_json)
                ciclo_json = serializers.serialize('json', MargenMensual.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                ciclo_list = json.loads(ciclo_json)
                unitario_json = serializers.serialize('json', Unitario.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                unitario_list = json.loads(unitario_json)
                costo_json = serializers.serialize('json', CostoTotal.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                costo_list = json.loads(costo_json)
                distr_json = serializers.serialize('json', CostoDistrSecAcum.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                distr_list = json.loads(distr_json)
                merch_json = serializers.serialize('json', CostoMerchAcum.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                merch_list = json.loads(merch_json)
                json_data = json.dumps({'meses': meses_dict, 'ciclo': ciclo_list, 'unitario': unitario_list, 'costo': costo_list, 'distr_sec': distr_list, 'merchandising': merch_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def carga_costo_venta_filtro(request, pk):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').filter(periodo__id=pk)[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                costo_json = CostoVentas.objects.values('claseCoste__clasecoste', 'costo', 'claseCoste__color').filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                costo_dict = ValuesQuerySetToDict(costo_json)
                json_data = json.dumps({'costo': costo_dict})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_tipoCliente(request):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').order_by('-periodo_id')[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#tipoCliente'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_tipoCliente_filtro(request, pk):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').filter(periodo__id=pk)[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#tipoCliente'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_sector(request):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').order_by('-periodo_id')[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#sector'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_sector_filtro(request, pk):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').filter(periodo__id=pk)[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#sector'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_tipoClienteSector(request):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').order_by('-periodo_id')[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#tipoClienteSector'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_tipoClienteSector_filtro(request, pk):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').filter(periodo__id=pk)[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#tipoClienteSector'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_sectores(request):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').order_by('-periodo_id')[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#sectores'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def hash_sectores_filtro(request, pk):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        periodo_vig = EERR.objects.values('periodo__periodo').filter(periodo__id=pk)[:1]
        for per in periodo_vig:
            periodo = per['periodo__periodo']
        for ofi in perfil:
            for of in ofi.oficina.all():
                hash_json = serializers.serialize('json', Hashtag.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).filter(hash='#sectores'))
                hash_list = json.loads(hash_json)
                json_data = json.dumps({'hash': hash_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def save_ingreso(user, report):
    ora = cx_Oracle.Connection(settings.DATABASES['default']['USER'] + '/' + settings.DATABASES['default']['PASSWORD'] + '@' + settings.DATABASES['default']['HOST'] + ':' + settings.DATABASES['default']['PORT'] + '/' + settings.DATABASES['default']['NAME'])
    cursor = ora.cursor()
    cursor.callproc('CONTROL_INGRESO', [user.id])
    cursor.callproc('PRIORIDADES')
    cursor.close()
    model = ControlIngreso()
    model.usuario = user
    model.reporte_id = report
    model.ingreso = datetime.now()
    model.save()