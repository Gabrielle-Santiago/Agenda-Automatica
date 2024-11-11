from django.http import HttpResponse
from django.core.mail import send_mail
from task.models import modelPerfume

# Envia o e-mail para o proprietário sobre a realização de um produto
def enviarEmail(request):
    # Obtém o último pedido de modelPerfume
    ultimoPedido = modelPerfume.objects.last()

    if ultimoPedido:
        # Coloca as informações, pois foram salvas somentes as iniciais no BD
        produto = ultimoPedido.get_product_display()
        aroma = ultimoPedido.get_aroma_display()
        quant = ultimoPedido.get_quant_display()

        mensagem = f"""
        Um novo pedido foi realizado, abaixo seguem as informações do produto:

        Produto: {produto}
        Aroma: {aroma}
        Quantidade: {quant}

        Aqui encontrassem as informações do cliente:

        Nome do cliente: {ultimoPedido.name}
        Número de contato: {ultimoPedido.numberContact}
        Email: {ultimoPedido.email}
        """
        
        send_mail(
            subject='Novo produto realizado',
            message=mensagem,
            from_email='email@gmail.com',  
            recipient_list=['email@gmail.com'],  
            fail_silently=False    
        )
        
        return HttpResponse('Email Enviado')
    else:
        return HttpResponse('Nenhum pedido encontrado')
    

def emailCliente(request):
    ultimoPedido = modelPerfume.objects.last()

    if ultimoPedido:
        # Coloca as informações, pois foram salvas somentes as iniciais no BD
        produto = ultimoPedido.get_product_display()
        aroma = ultimoPedido.get_aroma_display()
        quant = ultimoPedido.get_quant_display()

        mensagem = f"""
            Prezado(a), {ultimoPedido.name}!

            Informamos que seu pedido foi realizado com sucesso. Lembresse de que o produto comecará
            a ser produzido após o pagamento de 50% do valor total.

            Abaixo seguem as informações detalhadas do produto:

            Produto: {produto}
            Aroma: {aroma}
            Quantidade: {quant}

            Agradecemos pela confiança em nossos produtos. Estamos à disposição para qualquer dúvida
            ou informação adicional.
            Em caso de não ter efetuado o pagamento, entre em contato:

            Número de contato: (73) 98873-4003
            Email: Julianawacanda@outlook.com

            Atenciosamente,
            Espaço Bela Berillo
        """
        
        send_mail(
            subject='Confirmação do pedido!!',
            message=mensagem,
            from_email='email@gmail.com',  
            recipient_list=['email@gmail.com'],  
            fail_silently=False    
        )
        
        return HttpResponse('Email Enviado')
    else:
        return HttpResponse('Nenhum pedido encontrado')
    

# Envia o email para o cliente relembrando do agendamento
def confirmAgend(request):
    pedido = modelPerfume.objects.last()

    if pedido:

        mensagem = f"""
            Prezado(a) {pedido.name},

            Gostaríamos de confirmar o seu compromisso agendado com a profissional Juliana, conforme os detalhes a seguir:

            Data: ?
            Horário: ?
            Procedimento: ?

            Informações Importantes

            -> Pontualidade: Há uma tolerância de 10 minutos. Após esse período, o atendimento poderá ser cancelado, a menos que um aviso prévio seja dado.
            -> Pagamentos: O pagamento por PIX ou DINHEIRO deve ser feito presencialmente, no local do atendimento.
            -> Acompanhantes: Para procedimentos com itens perfurocortantes, pedimos que não tragam acompanhantes menores de idade.
            -> Cuidados com Procedimentos: Para procedimentos como micropigmentação, que envolvem tatuagens temporárias ou permanentes, recomenda-se atenção e paciência. Reserve um momento livre para garantir a melhor experiência.
            -> Taxas para Retornos: Caso haja a necessidade de retorno em data diferente da prevista, poderá ser cobrada uma taxa adicional.
            
            Formas de Pagamento

            -> Cartão de Débito/Crédito: Até 3x sem juros para valores a partir de R$300,00.
            -> PIX ou Dinheiro: 5% de desconto para valores a partir de R$100,00.
            -> Pagamentos com PIX ou dinheiro devem ser realizados no local do atendimento.

            Em caso de dúvidas, pagamentos antecipados ou informações adicionais, entre em contato:

            Número de contato: (73) 98873-4003
            Email: Julianawacanda@outlook.com

            Atenciosamente,
            Espaço Bela Berillo
        """
        
        send_mail(
            subject='Confirmação de Agendamento!!',
            message=mensagem,
            from_email='gabytestes659@gmail.com',  
            recipient_list=['gabytestes659@gmail.com'],  
            fail_silently=False    
        )
        
        return HttpResponse('Email Enviado')
    else:
        return HttpResponse('Nenhum pedido encontrado')