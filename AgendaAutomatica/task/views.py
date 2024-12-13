from datetime import datetime
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from enviarEmail.views import confirmAgend, emailCliente, enviarEmail, excluirPedido
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from task.forms import CadastroForm, formPerfume
from task.models import Cadastro
from .utils import validar_agendamento

def agenda(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data['data']
            horario = form.cleaned_data['horario']
            proced = form.cleaned_data['proced']

            try:
                validar_agendamento(data, horario, proced)
                form.save()
                confirmAgend(request)

                return JsonResponse({'success': True, 'message': 'Agendamento Confirmado! Qualquer dúvida entre em contato: (73) 98873-4003.'})

            except ValidationError as e:
                return JsonResponse({'success': False, 'message': e.message})
            
        else:
            return render(request, 'cadastros/cadastro.html', {
                'form': form,
                'error': 'Houve um erro. Tente Novamente!! Se persistir entre em contato: (73) 98873-4003.',
            })
    else:
        form = CadastroForm()

    return render(request, 'cadastros/cadastro.html', {'form': form})


class visualizarLista(ListView):
    model = Cadastro
    template_name = 'cadastros/cadastrados.html'
    context_object_name = 'cadastrados'
    

def pedidoPerfume(request):
    if request.method == 'POST':
        form = formPerfume(request.POST)

        if form.is_valid():   
            try:
                novoPedido = form.save()
                enviarEmail(novoPedido.id)
                emailCliente(request)
                excluirPedido(novoPedido.id)
                
                return JsonResponse({'success': True, 'message': 'Pedido Confirmado! Lembresse que o pedido só começará a ser feito mediante pagamento. Qualquer dúvida entre em contato: (73) 98873-4003.'})

            except ValidationError as e:
                return JsonResponse({'success': False, 'message': e.message})
        
        else:
            return render(request, 'auth/pedidoPerfume.html', {
                'form': form,
                'error': 'Houve um erro. Tente Novamente!! Se persistir entre em contato: (73) 98873-4003.',
            })
    else:
        form = formPerfume()

    return render(request, 'auth/pedidoPerfume.html', {'form':form})


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
            if user.is_superuser:
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


@login_required
def deletarAgendamento(request, id):
    cadastro = get_object_or_404(Cadastro, id=id)
    
    if request.method == 'POST':
        cadastro.delete()
        return redirect('cadastrados')
    return JsonResponse({'status': 'error', 'message': 'Requisição inválida'}, status=400)


def esqueciSenha(request):
    return render(request, 'main/esqueciSenha.html')


def indisponivel(request):
    return render(request, 'cadastros/indisponivel.html')


def saibaMais(request):
    return render(request, 'auth/saibaMais.html')