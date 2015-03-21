import cx_Oracle
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import auth
from light import settings

@login_required()
def logout(request):
    ora = cx_Oracle.Connection(settings.DATABASES['default']['USER'] + '/' + settings.DATABASES['default']['PASSWORD'] + '@' + settings.DATABASES['default']['HOST'] + ':' + settings.DATABASES['default']['PORT'] + '/' + settings.DATABASES['default']['NAME'])
    cursor = ora.cursor()
    cursor.callproc('CONTROL_INGRESO', [request.user.id])
    cursor.callproc('PRIORIDADES')
    cursor.close()
    auth.logout(request)
    return render(request, 'registration/logged_out.html')