from django.contrib import admin
from django.urls import path, include
from task import views
from task.views import visualizarLista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.agenda, name='agenda'),
    path('login_view/cadastros/cadastrados/', visualizarLista.as_view(), name='cadastrados'),
    path('cadastrados/', visualizarLista.as_view(), name='cadastrados'),
    path('pedidoPerfume/', views.pedidoPerfume, name='pedidoPerfume'),
    path('login_view/', views.login_view, name='login_view'),
    path('sair/', views.sair, name='sair'),
    path('sair/cadastros/cadastro', views.agenda, name='sair'),
    path('saibaMais/', views.saibaMais, name='saibaMais'),
    path('login_view/cadastros/cadastrados/<int:id>/', views.deletarAgendamento, name='deletarAgendamento'),
    path('cadastrados/deletarAgendamento/<int:id>/', views.deletarAgendamento, name='deletarAgendamento'),
    path('enviarEmail/', include('enviarEmail.urls')),
    path('enviarEmail/', views.enviarEmail, name='enviarEmail'),
]
