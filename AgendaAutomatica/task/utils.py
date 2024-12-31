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


def validarAgendamento(data, horario, proced):
    duracao = PROCEDURE_DURATIONS.get(proced)
    horarioInicial = datetime.combine(data, horario)
    horarioFinal = horarioInicial + duracao

    validarHorario(data, horarioInicial, horarioFinal)
    validarPausa(data, horarioInicial, horarioFinal)

    agendamentos = Cadastro.objects.filter(data=data)
    for agendamento in agendamentos:
        agendamentoInicio = datetime.combine(data, agendamento.horario)
        agendamentoFim = agendamentoInicio + PROCEDURE_DURATIONS.get(agendamento.proced)

        if horarioInicial < agendamentoFim and horarioFinal > agendamentoInicio:
            horariosDisponiveis = calcularHorarios(data, agendamentos)
            horariosFormatados = [f"{inicio.strftime('%H:%M')} - {fim.strftime('%H:%M')}" for inicio, fim in horariosDisponiveis]

            raise ValidationError(
                f"Horário indisponível. Horários disponíveis: {', '.join(horariosFormatados)}"
            )

    return True


def calcularHorarios(data, agendamentos):
    inicioTrabalho = datetime.combine(data, datetime.strptime("13:30", "%H:%M").time())
    fimTrabalho = datetime.combine(data, datetime.strptime("19:00", "%H:%M").time())
    pausaInicio = datetime.combine(data, datetime.strptime("15:30", "%H:%M").time())
    pausaFim = datetime.combine(data, datetime.strptime("16:30", "%H:%M").time())

    horariosDisponiveis = [(inicioTrabalho, pausaInicio), (pausaFim, fimTrabalho)]

    for agendamento in agendamentos:
        agendamentoInicio = datetime.combine(data, agendamento.horario)
        agendamentoFim = agendamentoInicio + PROCEDURE_DURATIONS.get(agendamento.proced)

        novosHorarios = []
        for inicio, fim in horariosDisponiveis:
            if agendamentoFim <= inicio or agendamentoInicio >= fim:
                novosHorarios.append((inicio, fim))
            else:
                if agendamentoInicio > inicio:
                    novosHorarios.append((inicio, agendamentoInicio))
                if agendamentoFim < fim:
                    novosHorarios.append((agendamentoFim, fim))
        horariosDisponiveis = novosHorarios

    return horariosDisponiveis


def validarHorario(data, horario_inicial, horario_final):
    inicio_trabalho = datetime.combine(data, datetime.strptime("13:30", "%H:%M").time())
    fim_trabalho = datetime.combine(data, datetime.strptime("19:00", "%H:%M").time())

    if horario_inicial < inicio_trabalho or horario_final > fim_trabalho:
        raise ValidationError("Horário fora do período de funcionamento. Tente outra data.")
    

    pausa_inicio = datetime.combine(data, datetime.strptime("15:30", "%H:%M").time())
    pausa_fim = datetime.combine(data, datetime.strptime("16:30", "%H:%M").time())

    if horario_inicial < pausa_fim and horario_final > pausa_inicio:
        raise ValidationError("O horário solicitado coincide com o intervalo da empresa. Tente a partir de 16:30.")


def validarPausa(data, horario_inicial, horario_final):
    pausa_inicio = datetime.combine(data, datetime.strptime("15:40", "%H:%M").time())
    pausa_fim = datetime.combine(data, datetime.strptime("16:20", "%H:%M").time())

    if horario_inicial < pausa_fim and horario_final > pausa_inicio:
        raise ValidationError("O horário solicitado coincide com o intervalo da empresa. Tente a partir de 16:30.")


def tempoAvaliacao(proced, horario):
    opcoesAvaliacao = ["SL", "LP", "LA", "PE", "ES", "NF", "RE", "MH"]
    
    if proced in opcoesAvaliacao:
        horario_ajustado = (datetime.combine(datetime.today(), horario) + timedelta(minutes=30)).time()
        return horario_ajustado
    
    return horario
