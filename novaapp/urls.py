# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('info/', views.info_view, name='info'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('', views.index_view, name='index'),
]