from django.contrib import admin
from django.urls import path
from task import views
from task.views import visualizarLista

# Caminhos utilizados durante o projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.agenda, name='agenda'),
    path('cadastrados/', visualizarLista.as_view(), name='cadastrados'),
]
