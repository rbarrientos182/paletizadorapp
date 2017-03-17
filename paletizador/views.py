from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Paletizador
from .models import Deposito
from .models import Zona
from .models import Region

def paletizador_edit(request):
    deposito = Deposito.objects.order_by('deposito')
    template = loader.get_template('paletizador.html')
    title = 'Configuracion Paletizador'
    context = {
        'deposito' : deposito,
        'title' : title
    }

    return HttpResponse(template.render(context, request))
