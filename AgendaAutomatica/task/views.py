from django.views.generic import ListView
from django.shortcuts import redirect, render
from task.forms import CadastroForm, IngredienteFormSet, formPerfume, formProduto
from task.models import Cadastro


# Função para registrar o cadastro no BD
def agenda(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            cadastro = Cadastro.objects.all()
            # Após cadastro encaminha para a lista de agendamento
            return redirect('cadastrados')
        
        else:
            return render(request, 'cadastro.html', {
                'form': form,
                'error' : 'Algo deu errado, tente novamente!!'
            })
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form':form})


# Utiliza do Generic Views do próprio Django para visualizar a lista
class visualizarLista(ListView):
    model = Cadastro
    template_name = 'cadastrados.html'
    context_object_name = 'cadastrados'
    

def pedidoPerfume(request):
    if request.method == 'POST':
        form = formPerfume(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'cadastro.html')
        
        else:
            return render(request, 'pedidoPerfume.html', {
                'form': form,
                'error': 'Algo deu errado, tente novamente!!'
            })
    else:
        form = formPerfume()

    return render(request, 'pedidoPerfume.html', {'form':form})


def cadastroProduto(request):
    if request.method == 'POST':
        produto_form = formProduto(request.POST)
        ingrediente_formset = IngredienteFormSet(request.POST)

        if produto_form.is_valid() and ingrediente_formset.is_valid():
            produto = produto_form.save()
            ingredientes = ingrediente_formset.save(commit=False)
             # Usar um conjunto para evitar duplicatas
            existing_ingredientes = set()
            
            for ingrediente in ingredientes:
                ingrediente.produto = produto  # Associa o ingrediente ao produto
                ingrediente.save() 
            return redirect('produtosCadastrados')

    else:
        produto_form = formProduto()
        ingrediente_formset = IngredienteFormSet()

    return render(request, 'cadastroProduto.html', {
        'form': produto_form,
        'ingrediente_formset': ingrediente_formset
    })


def produtosCadastrados(request):
    return render(request, 'produtosCadastrados.html')