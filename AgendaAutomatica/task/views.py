from django.views.generic import ListView
from django.shortcuts import render
from task.forms import CadastroForm
from task.models import Cadastro


# Função para registrar o cadastro no BD
def agenda(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            cadastro = Cadastro.objects.all()
            context = {
                'cadastro' : cadastro,
            }
            # Após cadastro encaminha para a lista de agendamento
            return render(request, 'cadastrados.html', context)
        
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
    return render(request, 'pedidoPerfume.html')