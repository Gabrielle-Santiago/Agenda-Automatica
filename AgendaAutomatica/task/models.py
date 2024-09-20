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
    OPTION_CHOICES = [
        ('perfume', 'Perfume'),
        ('hidratante', 'Hidratante'),
        ('peelins', 'Peelins'),
        ('antioxidante', 'Antioxidante'),
        ('outro', 'Outro'),
    ]

    # Aqui é referente aos cheiros
    CATEGORY_CHOICES = [
        ('floral','Floral'),
        ('citrico','Citrico'),
        ('amadeirado','Amadeirado'),
        ('outro1','Outro1'),
    ]

    # produto vai ser caso clique em outro e adicione o nome
    # produto = models.CharField(max_length=100, blank=True)

    # Referente as opções que já existem
    option = models.CharField(max_length=100, choices=OPTION_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.option} - {self.category}"
    

class Ingrediente(models.Model):
    produto = models.ForeignKey(modelProduto, on_delete=models.CASCADE, related_name='ingredientes')
    nome = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.quantidade}"