from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import *
from .forms import ArtigoForm, ComentarioForm


def index_view(request):
    artigos = Artigo.objects.all().order_by('-data_publicacao')
    context = {
        'artigos': artigos
    }
    return render(request, 'artigos/index.html', context)

def artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    pontuacao = artigo.avaliacoes.aggregate(Avg('pontuacao'))['pontuacao__avg']
    if pontuacao is not None:
        pontuacao = round(pontuacao, 1)
    comentarios = artigo.comentarios.all()
    comentario_form = ComentarioForm(request.POST or None)
    if request.method == 'POST' and comentario_form.is_valid():
        novo_comentario = comentario_form.save(commit=False)
        novo_comentario.artigo = artigo
        novo_comentario.save()
        return redirect('artigos:artigo', artigo_id=artigo.id)
    context = {
        'artigo': artigo,
        'pontuacao': pontuacao,
        'comentarios': comentarios,
        'comentario_form': comentario_form
    }
    return render(request, "artigos/artigo.html", context)

@login_required
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        novo_artigo = form.save(commit=False)
        novo_artigo.autor = request.user
        novo_artigo.save()
        return redirect('artigos:index')
    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user != artigo.autor:
        return redirect('artigos:artigo', artigo_id=artigo.id)
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:artigo', artigo_id=artigo.id)
    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user != artigo.autor:
        return redirect('artigos:artigo', artigo_id=artigo.id)
    artigo.delete()
    return redirect('artigos:index')

@login_required
def apaga_comentario_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    artigo_id = comentario.artigo.id
    if request.method == 'POST':
        comentario.delete()
        return redirect('artigos:artigo', artigo_id=artigo_id)
    return render(request, 'artigos/confirma_apagar_comentario.html', {'comentario': comentario})