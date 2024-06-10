from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas/', null=True, blank=True)
    info = models.TextField()
    biografia = models.TextField(default='', null=True, blank=True)  # Novo campo

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns')
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='bandas/', null=True, blank=True)
    ano_lancamento = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    titulo = models.CharField(max_length=100)
    duracao = models.DurationField()
    link = models.URLField(blank=True, null=True)
    letra = models.TextField(default='', null=True, blank=True)  # Novo campo

    def __str__(self):
        return self.titulo
