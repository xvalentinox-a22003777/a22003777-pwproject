from django.shortcuts import render

def index_view(request):
    return render(request, "novaapp/index.html")

def info_view(request):
    return render(request, "novaapp/info.html")

def contacto_view(request):
    return render(request, "novaapp/contacto.html")