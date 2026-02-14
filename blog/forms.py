from django import forms
from .models import Autor, Categoria, Post


class AutorFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"})
        }

class BusquedaPostFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
