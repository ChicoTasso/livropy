from django.forms import ModelForm, EmailField, Textarea, CharField
from .models import Autor, Livro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class AutorForm(ModelForm):

    def clean_idade(self):
        idade = self.cleaned_data['idade']

        if idade is not None and idade < 18:
            raise ValidationError('O autor não pode ter menos que 18 anos.', code='menor_idade')
        
        return idade
   
    class Meta:
        model=Autor
        fields='__all__'

class LivroForm(ModelForm):
   
    class Meta:
        model=Livro
        fields='__all__'

class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label='Nome')
    last_name = CharField(max_length=150, label='Sobrenome')
    email = EmailField(max_length=200, label='Email')

    class Meta:
        models = get_user_model()
        fields=['username','first_name','last_name','email','password1','password2']