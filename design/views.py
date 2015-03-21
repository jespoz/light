import json
import cx_Oracle
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from authenticated.models import Perfil, Prioridad
from data.models import FormulaDeIngreso
from design.models import DatosTimeline, Chat
from financials.models import MargenMensual
from financials.views import ValuesQuerySetToDict
from imports.models import Timeline
from light import settings


class IndexView(TemplateView):
    template_name = 'maqueta.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class TimelineView(TemplateView):
    template_name = 'timeline.html'

    def get_context_data(self, **kwargs):
        context = super(TimelineView, self).get_context_data(**kwargs)
        ora = cx_Oracle.Connection(settings.DATABASES['default']['USER'] + '/' + settings.DATABASES['default']['PASSWORD'] + '@' + settings.DATABASES['default']['HOST'] + ':' + settings.DATABASES['default']['PORT'] + '/' + settings.DATABASES['default']['NAME'])
        cursor = ora.cursor()
        cursor.callproc('CONTROL_INGRESO', [self.request.user.id])
        cursor.callproc('PRIORIDADES')
        cursor.close()
        time = []
        prioridad = []
        context['perfil'] = Perfil.objects.all().filter(usuario=self.request.user)
        context['datos_timeline'] = Timeline.objects.all().filter(usuario=self.request.user)[:5]
        for ofi in context['perfil']:
            for of in ofi.oficina.all():
                oficina = of.oficina
        for tm in context['datos_timeline']:
            valor = DatosTimeline.objects.all().filter(periodo=tm.periodo).filter(reporte=tm.reporte).filter(oficina__oficina=oficina)
            time.append({'reporte': tm.reporte, 'periodo': tm.periodo, 'actualizacion': tm.actualizacion, 'valor': valor, 'analista': tm.creado_por})
        context['timeline'] = time
        context['prioridades'] = Prioridad.objects.all().filter(usuario=self.request.user).order_by('-ingresos', '-promedio')[:3]
        for p in context['prioridades']:
            valor = DatosTimeline.objects.all().filter(reporte=p.reporte).filter(oficina__oficina=oficina).order_by('-id')[:1]
            prioridad.append({'reporte': p.reporte, 'valor': valor})
        context['prioridad'] = prioridad
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TimelineView, self).dispatch(*args, **kwargs)

class AccionableView(TemplateView):
    template_name = 'accionable.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccionableView, self).dispatch(*args, **kwargs)


def Acumulados(request, pk):
    if request.is_ajax():
        oficina = ''
        perfil = Perfil.objects.all().filter(usuario__username=request.user)
        for ofi in perfil:
                for of in ofi.oficina.all():
                    oficina = of.oficina
        if pk=='1':
            periodo = MargenMensual.objects.values('periodo__id').order_by('-id')[:1]
            for p in periodo:
                per = p['periodo__id']
            json_list = ValuesQuerySetToDict(MargenMensual.objects.values('periodo__periodo', 'ac').filter(oficina__oficina=oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id')[:6])
            json_data = json.dumps({'indicador': json_list})
        if pk=='6':
            periodo = FormulaDeIngreso.objects.values('periodo__id').order_by('-periodo__id')[:1]
            for p in periodo:
                per = p['periodo__id']
            json_list = ValuesQuerySetToDict(DatosTimeline.objects.extra(select={'ac': 'resultado'}).values('periodo__periodo', 'ac').filter(oficina__oficina=oficina, periodo__id__range=(per - 5, per)).order_by('periodo__id')[:6])
            json_data = json.dumps({'indicador': json_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def chat(request):
    if request.method == 'POST':
        comentario = Chat()
        comentario.autor = request.POST['autor']
        comentario.comentario = request.POST['comentario']
        comentario.save()
        chat_json = serializers.serialize('json', Chat.objects.all())
        chat_list = json.loads(chat_json)
        json_data = json.dumps({'chat': chat_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404