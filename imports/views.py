import json, csv
import cx_Oracle
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from data.models import FormulaDeIngreso
from financials.models import EERR, PrecioPromedio, Descuento, Gasto, Kilos
from imports.models import HistorialCreacionReporte, VentaCompleta
from reports.models import Reporte, Infografia
from master.models import Periodo

class ImportReport(TemplateView):
    template_name = 'imports/management.html'

    def get_context_data(self, **kwargs):
        context = super(ImportReport, self).get_context_data(**kwargs)
        context['infografias'] = Infografia.objects.all().order_by('id')
        context['reportes'] = Reporte.objects.all().order_by('id')
        context['periodos'] = Periodo.objects.all().order_by('-id')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImportReport, self).dispatch(*args, **kwargs)

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})

def data_exist_eerr(request, pk):
    consulta = EERR.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_pp_vs_zn(request, pk):
    consulta = PrecioPromedio.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_precio_desc(request, pk):
    consulta = Descuento.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_unit(request, pk):
    consulta = Gasto.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_formula_ingreso(request, pk):
    consulta = VentaCompleta.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def transformarKilos(kilos):
    return kilos.replace('KG', '').replace('.', '').replace(',', '.')

def transformarKilosSinKG(kilos):
    return kilos.replace('.', '').replace(',', '.')

def transformarNetos(netos):
    return netos.replace('.', '')

def transformarPrecios(netos):
    return netos.replace('CLP', '').replace('.', '')

def transformarPorcentajes(porcentajes):
    return porcentajes.replace('%', '').replace(',', '.')

def transformarFechas(fechas):
    fecha = fechas.replace('.', '/')
    retorno = fecha[6:] + "-" + fecha[3:5] + "-" + fecha[:2]
    return retorno

from datetime import datetime
from light import settings

def save_report(user, periodo, report):

    ora = cx_Oracle.Connection(settings.DATABASES['default']['USER'] + '/' + settings.DATABASES['default']['PASSWORD'] + '@' + settings.DATABASES['default']['HOST'] + ':' + settings.DATABASES['default']['PORT'] + '/' + settings.DATABASES['default']['NAME'])
    cursor = ora.cursor()
    model = HistorialCreacionReporte()
    model.usuario = user
    model.periodo_id = periodo
    model.actualizacion = datetime.now()
    model.reporte_id = report
    model.save()
    if report == 1:
        cursor.callproc('MARGEN_MENSUAL')
    elif report == 2:
        cursor.callproc('PESO_TIPO_CLIENTE')
    elif report == 3:
        cursor.callproc('PRECIO_PROMEDIO')
    elif report == 4:
        cursor.callproc('DESCUENTOS')
    elif report == 5:
        cursor.callproc('COSTOS_UNITARIOS')
    elif report == 6:
        cursor.callproc('CARGA_FORMULA_INGRESO')
        cursor.callproc('FORMULA_INGRESOS')
    cursor.callproc('TIMELINE')
    cursor.close()
