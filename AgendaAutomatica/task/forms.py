from django import forms
from .models import Cadastro, Ingrediente, modelPerfume, modelProduto

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
        fields = ['option', 'category']
        widgets = {
            'option': forms.Select(attrs={'class': 'form-select'})
        }
        category = {
            'category': forms.Select(attrs={'class': 'form-select'})
        }

    # Foi o chatGPT que fez, depois reviso
    def clean_option(self):
        option = self.cleaned_data.get('option')
        if len(option) > 50:  
            raise forms.ValidationError("O tamanho do campo 'option' é muito longo.")
        return option
    
# Formulário para o Produto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = modelProduto
        fields = ['option', 'category']

# Inline formset para Ingredientes
IngredienteFormSet = forms.inlineformset_factory(
    modelProduto, Ingrediente, 
    fields=['nome', 'quantidade'], 
    extra=1,  # Quantidade de forms extras (você pode adicionar mais dinamicamente)
    can_delete=True  # Permite que ingredientes possam ser removidos
)