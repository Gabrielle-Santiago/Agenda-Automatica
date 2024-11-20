from django.views.generic import ListView
from django.shortcuts import redirect, render
from enviarEmail.views import confirmAgend, emailCliente, enviarEmail
from task.forms import CadastroForm, formPerfume
from task.models import Cadastro
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Função para registrar o cadastro no BD
def agenda(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            confirmAgend(request)
            # Após cadastro encaminha para a lista de agendamento
            return redirect('cadastrados')
        
        else:
            print("Formulário inválido:", form.errors)
            return render(request, 'cadastros/cadastro.html', {
                'form': form,
                'error' : 'Algo deu errado, tente novamente!!'
            })
    else:
        form = CadastroForm()

    return render(request, 'cadastros/cadastro.html', {'form':form})



# Utiliza do Generic Views do próprio Django para visualizar a lista
class visualizarLista(ListView):
    model = Cadastro
    template_name = 'cadastros/cadastrados.html'
    context_object_name = 'cadastrados'
    

def pedidoPerfume(request):
    if request.method == 'POST':
        form = formPerfume(request.POST)

        if form.is_valid():
            form.save()
            enviarEmail(request)
            emailCliente(request)
            return render(request, 'cadastros/cadastro.html')
        
        else:
            return render(request, 'auth/pedidoPerfume.html', {
                'form': form,
                'error': 'Algo deu errado, tente novamente!!'
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


def indisponivel(request):
    return render(request, 'cadastros/indisponivel.html')