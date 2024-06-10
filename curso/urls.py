from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('curso/<int:curso_id>/', views.curso_view, name='curso'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('projeto/<int:projeto_id>/', views.projeto_view, name='projeto'),
    path('novo_curso/', views.novo_curso_view, name='novo_curso'),
    path('curso/<int:curso_id>/edita/', views.edita_curso_view, name='edita_curso'),
    path('curso/<int:curso_id>/apaga/', views.apaga_curso_view, name='apaga_curso'),
    path('nova_disciplina/', views.nova_disciplina_view, name='nova_disciplina'),
    path('disciplina/<int:disciplina_id>/edita/', views.edita_disciplina_view, name='edita_disciplina'),
    path('disciplina/<int:disciplina_id>/apaga/', views.apaga_disciplina_view, name='apaga_disciplina'),
    path('novo_projeto/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/<int:projeto_id>/edita/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/<int:projeto_id>/apaga/', views.apaga_projeto_view, name='apaga_projeto'),
]