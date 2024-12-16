from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from .models import Cadastro

PROCEDURE_DURATIONS = {
    "CH": timedelta(minutes=40), # Sobrancelhas COM henna
    "SH": timedelta(minutes=20), # Sobrancelhas SEM henna
    "LP": timedelta(minutes=90), # Limpeza de Pele
    "SL": timedelta(hours=1), # SPA Labial
    "DE": timedelta(minutes=40), # Depilação Buço e Axila
    "LA": timedelta(minutes=40), # Laminação dos fios
    "PE": timedelta(hours=1), # Peeling facial superficial
    "MH": timedelta(minutes=90), # Micro Henna
    "ES": timedelta(hours=2), # Estriderme
    "NF": timedelta(hours=1), # Nano Fios
    "RE": timedelta(minutes=50), # Revitalização Facial
}


def validar_agendamento(data, horario, proced):
    duracao = PROCEDURE_DURATIONS.get(proced)

    horario_inicial = datetime.combine(data, horario)
    horario_final = horario_inicial + duracao

    inicio_trabalho = datetime.combine(data, datetime.strptime("13:30", "%H:%M").time())
    fim_trabalho = datetime.combine(data, datetime.strptime("19:00", "%H:%M").time())

    if horario_inicial < inicio_trabalho or horario_final > fim_trabalho:
        raise ValidationError("Horário fora do período de funcionamento. Tente outra data.")

    pausa_inicio = datetime.combine(data, datetime.strptime("15:40", "%H:%M").time())
    pausa_fim = datetime.combine(data, datetime.strptime("16:20", "%H:%M").time())

    if horario_inicial < pausa_fim and horario_final > pausa_inicio:
        raise ValidationError("O horário solicitado coincide com o intervalo da empresa. Tente a partir 16:30min.")

    agendamentos = Cadastro.objects.filter(data=data)

    for agendamento in agendamentos:
        agendamento_inicio = datetime.combine(data, agendamento.horario)
        agendamento_fim = agendamento_inicio + PROCEDURE_DURATIONS.get(agendamento.proced)

        if horario_inicial < agendamento_fim and horario_final > agendamento_inicio:
            raise ValidationError("Horário indisponível para o procedimento solicitado.")


def validarIndisponibilidade(data):
    agendados =  Cadastro.objects.filter(data=data)

    if agendados.exists():
        raise ValidationError("agendados")
    else:
        raise ValidationError("nao agendados")