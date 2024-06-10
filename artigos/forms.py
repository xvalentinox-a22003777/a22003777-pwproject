from django import forms
from .models import Artigo, Comentario

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'imagem']

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do artigo'}),
            'conteudo': forms.Textarea(attrs={'placeholder': 'Conteúdo do artigo'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'conteudo']

        widgets = {
            'autor': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'conteudo': forms.Textarea(attrs={'placeholder': 'Seu comentário'}),
        }
