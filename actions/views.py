import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count, Avg, Sum
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, DetailView
from actions.models import AccLocal, Dispersion, AnalisisDescuentoTotales, AnalisisDescuentoApertura
from authenticated.models import Perfil
from data.models import FormulaDeIngreso
from financials.models import PesoTipoCliente
from financials.views import ValuesQuerySetToDict
from master.models import Periodo


class AccPrecioView(DetailView):
    template_name = 'precios.html'
    model = Periodo

    def get_context_data(self, **kwargs):
        context = super(AccPrecioView, self).get_context_data(**kwargs)
        context['periodo'] = AnalisisDescuentoTotales.objects.values('periodo__periodo', 'periodo__id').filter(periodo__id=self.get_object().pk)[:1]
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        periodo_id = 0
        for per in context['periodo']:
            periodo = per['periodo__periodo']
            periodo_id = per['periodo__id']
        context['periodo_id'] = periodo_id
        for ofi in context['perfil']:
            for of in ofi.oficina.all():
                periodo_anterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id - 1)
                for pa in periodo_anterior:
                    context['periodo_anterior'] = pa['periodo__id']
                periodo_posterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id + 1)
                for pa in periodo_posterior:
                    context['periodo_posterior'] = pa['periodo__id']
                return context

class AccLocalView(DetailView):
    template_name = 'locales.html'
    model = Periodo

    def get_context_data(self, **kwargs):
        context = super(AccLocalView, self).get_context_data(**kwargs)
        context['periodo'] = FormulaDeIngreso.objects.values('periodo__periodo', 'periodo__id').filter(periodo__id=self.get_object().pk)[:1]
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        for per in context['periodo']:
            periodo = per['periodo__periodo']
            periodo_id = per['periodo__id']
        for ofi in context['perfil']:
            for of in ofi.oficina.all():
                oficina = of.oficina
                periodo_anterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id - 1)
                for pa in periodo_anterior:
                    context['periodo_anterior'] = pa['periodo__id']
                periodo_posterior = PesoTipoCliente.objects.values('periodo__id').filter(oficina__oficina=of.oficina).annotate(dcount=Count('peso')).filter(periodo__id=periodo_id + 1)
                for pa in periodo_posterior:
                    context['periodo_posterior'] = pa['periodo__id']
        context['totales'] = AccLocal.objects.values('tipoCliente__tipo', 'tipoCliente__codigo', 'periodo__id').filter(oficina__oficina=oficina, periodo__periodo=periodo).annotate(dcount=Count('codLocal'), prom=Sum('ventaPromedio')).order_by('tipoCliente')
        context['adicional'] = AccLocal.objects.values('periodo__id').filter(oficina__oficina=oficina, periodo__periodo=periodo).annotate(suma=Sum('ventaPromedio'))
        if context['totales'].count() == 0:
            context['ancho'] = 0
        else:
            context['ancho'] = (100 / context['totales'].count()) - 1
        return context

@login_required
def accionable_filtro(request, pk, tc):
    if request.is_ajax():
        periodo = FormulaDeIngreso.objects.values('periodo__id').filter(periodo__id=pk)[:1]
        for p in periodo:
            per = p['periodo__id']
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for ofi in perfil:
            for of in ofi.oficina.all():
                oficina = of.oficina
        totales = AccLocal.objects.values('categoria__categoria').filter(oficina__oficina=oficina, periodo__periodo=per, tipoCliente__codigo=tc).exclude(categoria_id=19).annotate(dcount=Count('codLocal'), prom=Sum('ventaPromedio')).order_by('categoria')
        totales_dict = ValuesQuerySetToDict(totales)
        listado = AccLocal.objects.values('supervisor', 'preventa', 'codLocal', 'clienteLocal', 'categoria__categoria', 'sector__sector', 'promedio', 'minimo', 'maximo', 'ventaPromedio', 'semCalculo').filter(oficina__oficina=oficina, periodo__periodo='Semana 05.2015', tipoCliente__codigo=tc).order_by('-ventaPromedio')
        listado_dict = ValuesQuerySetToDict(listado)
        json_data = json.dumps({'totales': totales_dict, 'listado': listado_dict})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

@login_required
def dispersion_view(request, pk):
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for ofi in perfil:
            for of in ofi.oficina.all():
                listado_prev_crudos = Dispersion.objects.extra(select={'x': 'unidad', 'y': 'diferencia', 'dataLabels': 'material'}).values('dataLabels', 'x', 'y').filter(periodo__id=pk, oficina__oficina=of.oficina, negocio='CRUDO', responsable='Preventa')
                dict_prev_crudos = ValuesQuerySetToDict(listado_prev_crudos)
                listado_vend_crudos = Dispersion.objects.extra(select={'x': 'unidad', 'y': 'diferencia', 'dataLabels': 'material'}).values('dataLabels', 'x', 'y').filter(periodo__id=pk, oficina__oficina=of.oficina, negocio='CRUDO', responsable='Vendedor')
                dict_vend_crudos = ValuesQuerySetToDict(listado_vend_crudos)
                listado_prev_proc = Dispersion.objects.extra(select={'x': 'unidad', 'y': 'diferencia', 'dataLabels': 'material'}).values('dataLabels', 'x', 'y').filter(periodo__id=pk, oficina__oficina=of.oficina, negocio='PROCESADO', responsable='Preventa')
                dict_prev_proc = ValuesQuerySetToDict(listado_prev_proc)
                listado_vend_proc = Dispersion.objects.extra(select={'x': 'unidad', 'y': 'diferencia', 'dataLabels': 'material'}).values('dataLabels', 'x', 'y').filter(periodo__id=pk, oficina__oficina=of.oficina, negocio='PROCESADO', responsable='Vendedor')
                dict_vend_proc = ValuesQuerySetToDict(listado_vend_proc)
                json_data = json.dumps({'preventa_crudo' : dict_prev_crudos, 'vendedor_crudo': dict_vend_crudos, 'preventa_proc' : dict_prev_proc, 'vendedor_proc': dict_vend_proc})
                return HttpResponse(json_data, content_type='application/json; charset=utf8')


@login_required
def detalle_materiales(request, pk, ng):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        clase_json = ''
        for ofi in perfil:
            for of in ofi.oficina.all():
                if ng == '1':
                    clase_json = AnalisisDescuentoTotales.objects.values('sector__sector', 'codigoMaterial', 'material', 'conDescuento', 'sinDescuento', 'sobreprecio').filter(oficina__oficina=of.oficina, periodo__id=pk, sector__id__range=(1, 3)).order_by('sector__id', 'codigoMaterial')
                elif ng == '2':
                    clase_json = AnalisisDescuentoTotales.objects.values('sector__sector', 'codigoMaterial', 'material', 'conDescuento', 'sinDescuento', 'sobreprecio').filter(oficina__oficina=of.oficina, periodo__id=pk, sector__id__range=(4, 12)).order_by('sector__id', 'codigoMaterial')
                clase_list = ValuesQuerySetToDict(clase_json)
                json_data = json.dumps({'listado': clase_list})
                return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

@login_required
def detalle_materiales_apertura(request, pk, mt):
    if request.is_ajax():
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for ofi in perfil:
            for of in ofi.oficina.all():
                clase_json = AnalisisDescuentoApertura.objects.values('supervisor', 'preventa', 'codLocal', 'clienteLocal', 'categoria__categoria', 'responsable', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seisAdiez', 'onceAveinte', 'mayorVeinte').filter(oficina__oficina=of.oficina, periodo__id=pk, codigoMaterial=mt)
                clase_list = ValuesQuerySetToDict(clase_json)
                json_data = json.dumps({'listado': clase_list})
                return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404