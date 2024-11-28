from django.urls import path
from . import views

urlpatterns = [
    path('enviarEmail/', views.enviarEmail, name='enviarEmail'),
]