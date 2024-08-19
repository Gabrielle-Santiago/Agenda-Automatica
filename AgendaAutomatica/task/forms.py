# Cadastro das informações do formulário

from django import forms
from .models import Cadastro

# Classe que registra as informações contidas no modelo de cadastro
class CadastroForm(forms.ModelForm):
    
    class Meta:
        model = Cadastro
        fields = ['username', 'data', 'time', 'email', 'contact']