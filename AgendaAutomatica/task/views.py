from urllib import request
from django.shortcuts import render, redirect
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
            # Alterar para mandar para lista de agendamento
            return render(request, 'cadastro.html', context)
        
        else:
            return render(request, 'cadastro.html', {
                'form': form,
                'error' : 'Algo deu errado, tente novamente!!'
            })
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form':form})