from django.urls import path
from . import views

# Caminhos utilizados durante o projeto
urlpatterns = [
    path('enviarEmail/', views.enviarEmail, name='enviarEmail'),
]