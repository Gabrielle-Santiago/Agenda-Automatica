from django import forms
from .models import Cadastro, modelPerfume

# Essa área possui o cadastro das informações do formulário

# Classe que registra as informações contidas no modelo de cadastro
class CadastroForm(forms.ModelForm):
    
    class Meta:
        model = Cadastro
        fields = ['username', 'data', 'time', 'proced', 'email', 'contact']


class formPerfume(forms.ModelForm):
    
    class Meta:
        model = modelPerfume
        fields = ['product', 'aroma', 'quant', 'name', 'email', 'numberContact']
