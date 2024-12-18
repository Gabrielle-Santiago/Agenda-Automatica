from django.db import models

class Cadastro(models.Model):
     
    username = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    email = models.EmailField(max_length=240)
    contact = models.CharField(max_length=16)
    procediments = [
        ("CH", "sobrancelhas COM henna"),
        ("SH", "sobrancelhas SEM henna"),
        ("MH", "Micro Henna"),
        ("LP", "Limpeza de Pele"),
        ("SL", "SPA Labial"),
        ("DE", "Depilação Buço e Axila"),
        ("LA", "Laminação dos fios"),
        ("PE", "Peeling facial superficial"),        
        ("ES", "Estriderme"),
        ("NF", "Nano Fios"),
        ("RE", "Revitalização Facial"),
        ("DF", "Default"),
    ]

    proced = models.CharField(
        max_length = 2,
        choices = procediments,
        default = "DF",
    )

    def __str__(self):
        return f"{self.username} - {self.data} - {self.horario} - {self.proced} - {self.email} - {self.contact}"
    

class modelPerfume(models.Model):
    PRODUCT_CHOICES = [
        ("P", "Perfume"),
        ("H", "Hidratante"),
        ("A", "Antioxidante"),
        ("D", "Default"),
    ]
    
    AROMA_CHOICES = [
        ("F", "Floral"),
        ("C", "Citrico"),
        ("AM", "Amadeirado"),
        ("AD", "Adocidado"),
        ("D", "Default"),
    ]
    
    QUANT_CHOICES = [
        ("1", "10 ml"),
        ("3", "30 ml"),
        ("5", "50 ml"),
        ("10", "100 ml"),
        ("0", "0 ml"),
    ]
    
    product = models.CharField(
        max_length=1,
        choices=PRODUCT_CHOICES,
        default="D",
    )
    
    aroma = models.CharField(
        max_length=2,
        choices=AROMA_CHOICES,
        default="D",
    )
    
    quant = models.CharField(
        max_length=2,
        choices=QUANT_CHOICES,
        default="0",
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    numberContact = models.CharField(max_length=16, default="000000000")

    def __str__(self):
        return f"{self.product} - {self.aroma} - {self.quant} - {self.name} - {self.email} - {self.numberContact}"
    

class modelIndisponivel(models.Model):
    data = models.DateField()
    horarioInicio = models.TimeField()
    horarioFim = models.TimeField()

    def __str__(self):
        return f"{self.data} - {self.horarioInicio} - {self.horarioFim}"