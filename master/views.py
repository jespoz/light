import StringIO
import codecs
import csv
import json
import cx_Oracle
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from imports.views import transformarFechas
from light import settings
from master.models import LocalesNulos, Cliente


class RevisionLocales(TemplateView):
    template_name = 'maestros/revision.html'

def ejecutar_nulos(request):
    ora = cx_Oracle.Connection(settings.DATABASES['default']['USER'] + '/' + settings.DATABASES['default']['PASSWORD'] + '@' + settings.DATABASES['default']['HOST'] + ':' + settings.DATABASES['default']['PORT'] + '/' + settings.DATABASES['default']['NAME'])
    cursor = ora.cursor()
    cursor.callproc('LOCALES_NO_MAESTRO')
    cursor.close()
    consulta = serializers.serialize('json', LocalesNulos.objects.all().order_by('cliente'))
    carga = json.loads(consulta)
    json_data = json.dumps({'locales': carga})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

# -*- coding: utf-8 -*-
import chardet

def import_file(request):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            content = file.read()
            encoding = chardet.detect(content)['encoding']
            if encoding != 'utf-8':
                content = content.decode(encoding, 'replace').encode('utf-8')
            filestream = StringIO.StringIO(content)
            dialect = csv.Sniffer().sniff(content)
            mod_csv = csv.DictReader(filestream.read().splitlines(), dialect=dialect)
            for x in mod_csv:
                model = Cliente()
                model.codigo = x['Codigo']
                model.cliente = x['Nombre 1']
                model.direccion = x['Nombre 2']
                model.poblacion = x['Poblacion']
                model.creacion = transformarFechas(x['Fecha'])
                model.save()
                mensaje = 'Los clientes han sido actualizados correctamente'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})