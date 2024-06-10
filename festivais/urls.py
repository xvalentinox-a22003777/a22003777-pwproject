from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('', views.lista_festivais, name='lista_festivais'),
    path('festival/<int:id>/', views.detalhe_festival, name='detalhe_festival'),
]