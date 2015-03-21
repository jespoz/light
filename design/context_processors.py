from authenticated.models import Perfil
from design.models import Acceso

def menu(request):
    context = []
    try:
        perfil = Perfil.objects.all().filter(usuario=request.user)
        for perfil in perfil:
            context = {
                'accesos': Acceso.objects.all().filter(cargo=perfil.cargo)
            }
    except:
        context = {
            'accesos': 'Error'
        }
    return context

def chat(request):
    try:
        context = {
            'analistas': Perfil.objects.all().filter(cargo_id=61)
        }
    except:
        context = {
            'analistas': 'Error'
        }
    return context