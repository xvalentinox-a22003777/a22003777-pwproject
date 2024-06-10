from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# noobsite/views.py

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view_error(request):
    return HttpResponse("404 Page Not Found \n \n \n Sorry n00b!")

def index_view_wow(request):
    return HttpResponse("W0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0W\nW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0WW0W0W0W0W")

def index_view_msg(request):
    return HttpResponse("WeLcOmE tO tHiS pAgE, iTs AwEsOmE")
