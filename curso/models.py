from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return f"Curso: {self.apresentacao}"

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f"Área Científica: {self.nome}"

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=200)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

    def __str__(self):
        return f"Disciplina: {self.nome}"

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='curso/projetos', null=True, blank=True)
    video_youtube = models.URLField(null=True, blank=True)
    repositorio_github = models.URLField(null=True, blank=True)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"Projeto: {self.nome} / {self.disciplina} "

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=200)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return f"Linguagem de Programação: {self.nome}"

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return f"Docente: {self.nome}"

