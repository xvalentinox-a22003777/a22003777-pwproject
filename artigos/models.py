from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()

    def __str__(self):
        return self.usuario.username

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='artigos/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário por {self.autor} em {self.artigo.titulo}"

class Avaliacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='avaliacoes')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"{self.pontuacao} por {self.autor.username} em {self.artigo.titulo}"
