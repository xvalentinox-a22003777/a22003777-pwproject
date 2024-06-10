from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def lista_festivais(request):
    localizacaos = Localizacao.objects.all()
    context = {
        'localizacaos': localizacaos
    }
    return render(request, 'festivais/festivais.html', context)


def detalhe_festival(request, id):
    festival = get_object_or_404(Festival, id=id)
    context = {
        'festival': festival
    }
    return render(request, 'festivais/detalhe.html', context)