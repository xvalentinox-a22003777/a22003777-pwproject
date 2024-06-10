from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CursoForm, DisciplinaForm, ProjetoForm


def index_view(request):
    cursos = Curso.objects.all()
    disciplinas = Disciplina.objects.all()
    projetos = Projeto.objects.all()

    disciplinas_por_ano = {}
    for disciplina in disciplinas:
        ano = disciplina.ano
        if ano not in disciplinas_por_ano:
            disciplinas_por_ano[ano] = []
        disciplinas_por_ano[ano].append(disciplina)

    context = {
        'cursos': cursos,
        'disciplinas' : disciplinas,
        'disciplinas_por_ano': disciplinas_por_ano,
        'projetos' : projetos
    }
    return render(request, 'curso/index.html', context)

def curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    context = {
        'curso': curso
    }
    return render(request, 'curso/curso.html', context)

def projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    context = {
        'projeto': projeto
    }
    return render(request, 'curso/projeto.html', context)

def disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    linguagens = LinguagemProgramacao.objects.filter(projetos__in=projetos).distinct()

    context = {
        'disciplina': disciplina,
        'projetos': projetos,
        'linguagens': linguagens,
    }
    return render(request, 'curso/disciplina.html', context)

@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:index')
    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)

@login_required
def edita_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('curso:curso', curso_id=curso.id)
    context = {'form': form, 'curso': curso}
    return render(request, 'curso/edita_curso.html', context)

@login_required
def apaga_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('curso:index')

@login_required
def nova_disciplina_view(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:index')
    context = {'form': form}
    return render(request, 'curso/nova_disciplina.html', context)

@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('curso:disciplina', disciplina_id=disciplina.id)
    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'curso/edita_disciplina.html', context)

@login_required
def apaga_disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    disciplina.delete()
    return redirect('curso:index')

@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('curso:index')
    context = {'form': form}
    return render(request, 'curso/novo_projeto.html', context)

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('curso:projeto', projeto_id=projeto.id)
    context = {'form': form, 'projeto': projeto}
    return render(request, 'curso/edita_projeto.html', context)

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('curso:index')

