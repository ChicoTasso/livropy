from django.forms import ModelForm
from .models import Autor, Livro


class AutorForm(ModelForm):
   
    class Meta:
        model=Autor
        fields='__all__'

class LivroForm(ModelForm):
   
    class Meta:
        model=Livro
        fields='__all__'