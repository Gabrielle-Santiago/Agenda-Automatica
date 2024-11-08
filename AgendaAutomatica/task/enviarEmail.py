from models import modelPerfume
from django.core.mail import send_mass_mail

# Essa área foca no envio dos emails
def enviarEmail():
    message1 = (
        "Efetuado o pedido de um produto!!",
        "Um novo produto foi pedido, abaixo segue as informações do produto:",
        "dreamsdegaby@gmail.com",  # Remetente
        ["dreamsdegaby@gmail.com"],
        print("Mensagem 0 enviada com sucesso")
    )
    message2 = (
        "Confirmação do pedido",
        "Seu pedido foi realizado com sucesso. Lembresse de que o produto começará a ser feito após 50'%' do valor, caso ainda não tenha realizado entre em contato com seguinte número: (73) 98888-7777.",
        "seu_email@gmail.com",
        ["destinatario3@gmail.com"],
    )
    
    send_mass_mail((message1, message2), fail_silently=False)


# def enviar_email(destinatario, assunto, mensagem):
    
#     # Configuração do servidor
#     smtp_server = "smtp.gmail.com" 
#     smtp_port = 587
#     remetente = "dreamsdegaby@gmail.com"  # O e-mail do proprietário
#     senha = "puwn xpyb awox onso"  # A senha do e-mail

#     # Criação do e-mail
#     msg = MIMEMultipart()
#     msg["From"] = remetente
#     msg["To"] = destinatario
#     msg["Subject"] = assunto

#     # Adiciona o corpo da mensagem
#     msg.attach(MIMEText(mensagem, "plain"))

#     try:
#         # Conecta ao servidor
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()  # Inicia a conexão segura
#         server.login(remetente, senha) 

#         # Envia o e-mail
#         server.sendmail(remetente, destinatario, msg.as_string())
#         print("Email enviado com sucesso.")

#     except Exception as e:
#         print(f"Houve um erro: {e}")

#     finally:
#         server.quit()  # Fecha a conexão com o servidor SMTP


# enviar_email("dreamsdegaby@gmail.com", "Efetuado o pedido de um produto!!", "Um novo produto foi pedido, abaixo segue as informações do produto:  Produto: ")

# f"""
#     Um novo produto foi pedido, abaixo segue as informações do produto:
#     Produto: {modelPerfume.product}
#     Aroma: {modelPerfume.aroma}
#     Quantidade: {modelPerfume.quant}
#     Nome do cliente: {modelPerfume.name}
#     Contato: {modelPerfume.numberContact}
#     Email: {modelPerfume.email}
#     """