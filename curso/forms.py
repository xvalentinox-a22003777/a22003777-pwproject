from django import forms
from .models import Curso, Disciplina, Projeto

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'apresentacao', 'objetivos', 'competencias']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do curso'}),
            'apresentacao': forms.Textarea(attrs={'placeholder': 'Apresentação do curso'}),
            'objetivos': forms.Textarea(attrs={'placeholder': 'Objetivos do curso'}),
            'competencias': forms.Textarea(attrs={'placeholder': 'Competências do curso'}),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'curricularIUnitReadableCode', 'area_cientifica']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da disciplina'}),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'conceitos_aplicados', 'tecnologias_usadas', 'imagem', 'video_youtube', 'repositorio_github', 'disciplina']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do projeto'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição do projeto'}),
            'conceitos_aplicados': forms.Textarea(attrs={'placeholder': 'Conceitos aplicados'}),
            'tecnologias_usadas': forms.Textarea(attrs={'placeholder': 'Tecnologias usadas'}),
        }
