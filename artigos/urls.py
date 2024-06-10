from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('novo/', views.novo_artigo_view, name='novo_artigo'),
    path('artigo/<int:artigo_id>/edita/', views.edita_artigo_view, name='edita_artigo'),
    path('artigo/<int:artigo_id>/apaga/', views.apaga_artigo_view, name='apaga_artigo'),
    path('comentario/<int:comentario_id>/apaga/', views.apaga_comentario_view, name='apaga_comentario'),
]