## O SCRIPT TEM COMO OBJETIVO ENVIAR UMA MENSAGEM NO E-MAIL NO DOMÍNIO GMAIL VIA PYTHON
import os
import smtplib
from email.message import EmailMessage
from segredos import senha


# Configurar email, senha
EMAIL_ADDRESS = 'tiago.soares@gennesys.com'
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['Subject'] = 'E-mail Teste' # Assunto
msg['From'] = 'tiago.soares@gennesys.com' # De 
msg['To'] = 'tiago.soares@gennesys.com' # Destino
msg.set_content('Olá sou um código Python') #msg


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
