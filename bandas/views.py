from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BandaForm, AlbumForm, MusicaForm
# Create your views here.

def index_view(request):
    bandas = Banda.objects.all()
    context = {
        'bandas': bandas
    }
    return render(request, 'bandas/index.html', context)

def banda_view(request, banda_id):
    context = {
        'banda': Banda.objects.get(id=banda_id),
    }
    return render(request, "bandas/banda.html", context)

def album_view(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
    }
    return render(request, "bandas/album.html", context)

def musica_view(request, musica_id):
    context = {
        'musica': Musica.objects.get(id=musica_id),
    }
    return render(request, "bandas/musica.html", context)

@login_required
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')
    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    form = BandaForm(request.POST or None, request.FILES or None, instance=banda)
    if form.is_valid():
        form.save()
        return redirect('bandas:banda', banda_id=banda.id)
    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    banda.delete()
    return redirect('bandas:index')

def novo_album_view(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        novo_album = form.save(commit=False)
        novo_album.banda = banda
        novo_album.save()
        return redirect('bandas:banda', banda_id=banda.id)
    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/novo_album.html', context)

@login_required
def edita_album_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    form = AlbumForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('bandas:album', album_id=album.id)
    context = {'form': form, 'album': album}
    return render(request, 'bandas/edita_album.html', context)

@login_required
def apaga_album_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    banda_id = album.banda.id
    album.delete()
    return redirect('bandas:banda', banda_id=banda_id)

@login_required
def nova_musica_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    form = MusicaForm(request.POST or None)
    if form.is_valid():
        nova_musica = form.save(commit=False)
        nova_musica.album = album
        nova_musica.save()
        return redirect('bandas:album', album_id=album.id)
    context = {'form': form, 'album': album}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    form = MusicaForm(request.POST or None, instance=musica)
    if form.is_valid():
        form.save()
        return redirect('bandas:musica', musica_id=musica.id)
    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
def apaga_musica_view(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    album_id = musica.album.id
    musica.delete()
    return redirect('bandas:album', album_id=album_id)