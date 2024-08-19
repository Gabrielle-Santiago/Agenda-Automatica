from django.db import models

# Modelos

class Cadastro(models.Model):
     
    # Ordenando os tipos referente a cada informação recebida do formulário de cadastro

    username = models.CharField(max_length=100)
    data = models.DateField()
    time = models.TimeField()
    email = models.EmailField(max_length=240)
    contact = models.CharField(max_length=16)

    def __str__(self):
        # Retorna os tipos salvo no modelo
        return f"{self.username} - {self.data} - {self.time} - {self.email} - {self.contact}"