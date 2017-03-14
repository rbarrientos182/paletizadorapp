from django.shortcuts import render

from .models import Paletizador
from .models import Deposito

def paletizador_edit(arg):
    deposito = Deposito.objects.order_by('idDeposito')
    template = loader.get_template('paletizador.html')
    title = 'Configuración Paletizador'
    context = {
        'deposito' : deposito,
        'title' : title
    }

    return HttpResponse(template.render(context, request))
