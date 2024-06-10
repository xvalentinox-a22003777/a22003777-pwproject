from bandas.models import *
import json
from datetime import timedelta

def parse_duration(duracao_str):
    partes = duracao_str.split(':')
    if len(partes) == 3:
        horas, minutos, segundos = map(int, partes)
    elif len(partes) == 2:
        horas = 0
        minutos, segundos = map(int, partes)
    else:
        raise ValueError("Formato de duração inválido: " + duracao_str)

    return timedelta(hours=horas, minutes=minutos, seconds=segundos)

Banda.objects.all().delete()
Musica.objects.all().delete()
Album.objects.all().delete()
# Carregar e criar as bandas
with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)
    for banda in bandas:
        Banda.objects.create(
            nome=banda['nome'],
            info=f"Nacionalidade: {banda['nacionalidade']}, Ano de Criação: {banda['ano_criacao']}"
        )

# Carregar e criar os álbuns e músicas
with open('bandas/json/albuns.json') as f:
    albuns = json.load(f)
    for album in albuns:
        banda_obj = Banda.objects.get(nome=album['banda'])
        album_obj = Album.objects.create(
            banda=banda_obj,
            titulo=album['titulo'],
            ano_lancamento=album['ano_lancamento']
        )

        for musica in album['musicas']:
            duracao_timedelta = parse_duration(musica['duracao'])
            Musica.objects.create(
                album=album_obj,
                titulo=musica['titulo'],
                duracao=duracao_timedelta
            )
