from django.contrib import admin
from django.urls import path
from task import views
from task.views import visualizarLista

# Caminhos utilizados durante o projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.agenda, name='agenda'),
    path('login_view/cadastros/cadastrados/', visualizarLista.as_view(), name='cadastrados'),
    path('cadastrados/', visualizarLista.as_view(), name='cadastrados'),
    path('pedidoPerfume/', views.pedidoPerfume, name='pedidoPerfume'),
    path('cadastroProduto/', views.cadastroProduto, name='cadastroProduto'),
    path('produtosCadastrados/', views.produtosCadastrados, name='produtosCadastrados'),
    path('login_view/', views.login_view, name='login_view'),
    path('login/esqueciSenha/', views.esqueciSenha, name='esqueciSenha'),
    path('sair/', views.sair, name='sair'),
    path('sair/cadastros/cadastro', views.agenda, name='sair'),
]
