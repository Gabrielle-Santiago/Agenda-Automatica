from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from task.forms import CadastroForm, IngredienteFormSet, formPerfume, formProduto
from task.models import Cadastro, modelProduto
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            return render(request, 'cadastros/cadastro.html', {
                'form': form,
                'error' : 'Algo deu errado, tente novamente!!'
            })
    else:
        form = CadastroForm()

    return render(request, 'cadastros/cadastro.html', {'form':form})



# Utiliza do Generic Views do próprio Django para visualizar a lista
# Está dando erro para conferir somente com login
class visualizarLista(ListView):
    model = Cadastro
    template_name = 'cadastros/cadastrados.html'
    context_object_name = 'cadastrados'
    

def pedidoPerfume(request):
    if request.method == 'POST':
        form = formPerfume(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'cadastros/cadastro.html')
        
        else:
            return render(request, 'auth/pedidoPerfume.html', {
                'form': form,
                'error': 'Algo deu errado, tente novamente!!'
            })
    else:
        form = formPerfume()

    return render(request, 'auth/pedidoPerfume.html', {'form':form})


@login_required
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

    return render(request, 'cadastros/cadastroProduto.html', {
        'form': produto_form,
        'ingrediente_formset': ingrediente_formset
    })


@login_required
def produtosCadastrados(request):
    return render(request, 'auth/produtosCadastrados.html')


def filtrar_produtos(request):
    produto = request.GET.get('produto', None)
    aroma = request.GET.get('aroma', None)

    # Filtrar os produtos baseado nas escolhas do usuário
    produtos = modelProduto.objects.all()

    if produto:
        produtos = produtos.filter(option=produto)
    if aroma:
        produtos = produtos.filter(category=aroma)

    # Retornar a lista de nomes dos produtos filtrados
    produtos_filtrados = list(produtos.values_list('option', 'category'))

    return JsonResponse({'produtos': produtos_filtrados})


def produto_detalhes(request, produto_id):
    produto = get_object_or_404(modelProduto, id=produto_id)
    ingredientes = produto.ingredientes.all()

    ingredientes_data = list(ingredientes.values('nome', 'quantidade'))

    return JsonResponse({
        'option': produto.option,
        'category': produto.category,
        'ingredientes': ingredientes_data
    })


def login_view(request):
    if request.method == 'GET':
        return render(request, 'main/login.html', {'form': AuthenticationForm()})
    
    else:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'main/login.html', {
                'form': AuthenticationForm(),
                'error': 'Email ou senha estão incorretos!!'
            })
        else:
            if user.is_superuser:  # Verifica se é o superusuário
                login(request, user)
                return redirect('cadastros/cadastrados')
            else:
                return render(request, 'main/login.html', {
                    'form': AuthenticationForm(),
                    'error': 'Acesso restrito ao administrador!'
                })


@login_required
def sair(request):
    logout(request)
    return redirect('cadastros/cadastro')

def esqueciSenha(request):
    return render(request, 'main/esqueciSenha.html')