from django.views.generic import ListView
from django.shortcuts import redirect, render
from task.forms import CadastroForm, formPerfume
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
    return render(request, 'cadastroProduto.html')


def produtosCadastrados(request):
    return render(request, 'produtosCadastrados.html')