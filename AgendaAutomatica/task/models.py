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
    

class modelPerfume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    adress = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email} - {self.adress}"


class modelProduto(models.Model):
    OPTION_CHOICE = [
        ('op1', 'Opcao 1'),
        ('op2', 'Opcao 2'),
        ('op3', 'Opcao 3'),
        ('op4', 'Opcao 4'),
        ('op5', 'Opcao 5'),
    ]

    option = models.CharField(
    max_length=4,
    choices=OPTION_CHOICE,
    default='op1',
    )

    def __str__(self):
        return f"{self.option}"