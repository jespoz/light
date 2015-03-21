import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from authenticated.models import Perfil
from django.db.models import Avg, Count
from django.views.generic import TemplateView, DetailView
from financials.views import save_ingreso
from .models import *
from financials.models import PesoTipoCliente
from reports.models import Infografia


class FormulaIngreso(TemplateView):
    template_name = 'infographic/formulaIngreso.html'

    def get_context_data(self, **kwargs):
        context = super(FormulaIngreso, self).get_context_data(**kwargs)
        save_ingreso(self.request.user, 6)
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        context['periodo'] = FormulaDeIngreso.objects.values('periodo__periodo', 'periodo__id').order_by('-periodo_id')[:1]
        context['informacion'] = Infografia.objects.all().filter(id=2)
        periodo = ''
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
                context['totales'] = FI_Totales.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['comparativo'] = FI_Comparativo.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['tipoCliente'] = PesoTipoCliente.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('id')
                context['precios'] = FI_DetallePrecio.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['locales'] = FI_Locales.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['nuevos'] = FI_LocalesNuevos.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['recuperados'] = FI_LocalesRecuperados.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['fugados'] = FI_LocalesFugados.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['fa_locales'] = IconosLocales.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['frecuencia'] = FI_DetalleFrecuencia.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('categoria')
                context['ticket'] = FI_DetalleTicket.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('id')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FormulaIngreso, self).dispatch(*args, **kwargs)

class FormulaIngresoFiltro(DetailView):
    template_name = 'infographic/formulaIngreso.html'
    model = Periodo

    def get_context_data(self, **kwargs):
        context = super(FormulaIngresoFiltro, self).get_context_data(**kwargs)
        save_ingreso(self.request.user, 6)
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        context['periodo'] = FormulaDeIngreso.objects.values('periodo__periodo', 'periodo__id').filter(periodo__id=self.get_object().pk)[:1]
        context['informacion'] = Infografia.objects.all().filter(id=2)
        periodo = ''
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
                context['totales'] = FI_Totales.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['comparativo'] = FI_Comparativo.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['tipoCliente'] = PesoTipoCliente.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('id')
                context['precios'] = FI_DetallePrecio.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['locales'] = FI_Locales.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['nuevos'] = FI_LocalesNuevos.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['recuperados'] = FI_LocalesRecuperados.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['fugados'] = FI_LocalesFugados.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['fa_locales'] = IconosLocales.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo)
                context['frecuencia'] = FI_DetalleFrecuencia.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('categoria')
                context['ticket'] = FI_DetalleTicket.objects.all().filter(oficina__oficina=of.oficina).filter(periodo__periodo=periodo).order_by('id')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FormulaIngresoFiltro, self).dispatch(*args, **kwargs)

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def carga_ventas_acumuladas(request):
    if request.is_ajax():
        periodo = FI_Totales.objects.values('periodo__id').order_by('-periodo_id')[:1]
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for p in periodo:
            per = p['periodo__id']
        for ofi in perfil:
            for of in ofi.oficina.all():
                semanas_json = FI_Totales.objects.values('periodo__periodo', 'periodo__id').filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id')
                semanas_dict = ValuesQuerySetToDict(semanas_json)
                ventas_json = serializers.serialize('json', FI_Totales.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                ventas_list = json.loads(ventas_json)
                json_data = json.dumps({'semanas': semanas_dict, 'ventas': ventas_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def carga_ventas_acumuladas_filtro(request, pk):
    if request.is_ajax():
        periodo = FormulaDeIngreso.objects.values('periodo__id').filter(periodo__id=pk)[:1]
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for p in periodo:
            per = p['periodo__id']
        for ofi in perfil:
            for of in ofi.oficina.all():
                semanas_json = FI_Totales.objects.values('periodo__periodo', 'periodo__id').filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id')
                semanas_dict = ValuesQuerySetToDict(semanas_json)
                ventas_json = serializers.serialize('json', FI_Totales.objects.all().filter(oficina__oficina=of.oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id'))
                ventas_list = json.loads(ventas_json)
                json_data = json.dumps({'semanas': semanas_dict, 'ventas': ventas_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404