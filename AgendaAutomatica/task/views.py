from urllib import request
from django.shortcuts import render, redirect

# Create your views here.
def agenda(request):
    return render(request, 'cadastro.html')