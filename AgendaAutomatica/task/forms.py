from django import forms
from .models import Cadastro, modelPerfume, modelProduto

# Essa área possui o cadastro das informações do formulário

# Classe que registra as informações contidas no modelo de cadastro
class CadastroForm(forms.ModelForm):
    
    class Meta:
        model = Cadastro
        fields = ['username', 'data', 'time', 'email', 'contact']


class formPerfume(forms.ModelForm):
    
    class Meta:
        model = modelPerfume
        fields = ['name', 'email', 'adress']


class formProduto(forms.ModelForm):

    class Meta:
        model = modelProduto
        fields = ['option']