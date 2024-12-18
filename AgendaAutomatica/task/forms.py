from django import forms
from .models import Cadastro, modelIndisponivel, modelPerfume

class CadastroForm(forms.ModelForm):
    
    class Meta:
        model = Cadastro
        fields = ['username', 'data', 'horario', 'proced', 'email', 'contact']
        

class formPerfume(forms.ModelForm):
    
    class Meta:
        model = modelPerfume
        fields = ['product', 'aroma', 'quant', 'name', 'email', 'numberContact']


class formIndisponivel(forms.ModelForm):

    class Meta:
        model = modelIndisponivel
        fields = ['data', 'horarioInicio', 'horarioFim']