from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index, name='index'),
    path('previsao/', views.previsao, name='previsao'),
    path('previsao_5_dias/', views.previsao_5_dias, name='previsao_5_dias'),  # Nova rota
    path('api/cidades/', views.lista_cidades, name='lista_cidades'),
    path('api/previsao_hoje/<int:cidade_id>/', views.previsao_hoje, name='previsao_hoje'),
    path('api/previsao_cinco_dias/<int:cidade_id>/', views.previsao_cinco_dias, name='previsao_cinco_dias'),
    path('api_documentation/', views.api_documentation, name='api_documentation'),
]
