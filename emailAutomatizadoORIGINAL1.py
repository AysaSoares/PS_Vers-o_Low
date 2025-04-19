import smtplib
from email.message import EmailMessage
import pdb
import getpass

nome = sasa
email_remetente = input("Digite seu e-mail: ")
senha = getpass.getpass("Digite sua senha: ")
email_destinatario = input("E-mail do destinatário: ")
assunto = input("Título do e-mail: ")
mensagem = input("Mensagem: ")
lista_de_emails = email_destinatario.split( )

for email in lista_de_emails:
    msg = EmailMessage()
    msg['From'] = email_remetente
    msg['To'] = email
    msg['Subject'] = assunto
    msg.set_content(mensagem)
    pdb.set_trace()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_remetente, senha)
            server.send_message(msg)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")

