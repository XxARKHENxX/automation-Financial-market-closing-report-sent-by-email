# import win32com.client as win32

# # smtplib - Enviar email usando outras formas


# def SendMail(Ibovespa, Dolar, SeP500):


#     outlook = win32.Dispatch("outlook.application")

#     email = outlook.CreateItem(0)
#     # email.To = "evento@varos.com.br"
#     email(
#         To = "evento@varos.com.br",
#         subject = "Relatório de Mercado",
#         Body = f''' Preazado diretor, segue o relatório de mercado: 
#                 * O Ibovespa teve o retorno de {Retorno_Ibovespa}
#                 * O Dólar teve o retorno de {Retorno_Dolar}
#                 * O S&P500 teve o retorno de {Retorno_SeP500}

#                 segue em anexo a performance dos ativos nos últimos 6 meses


#                 att, 
#                 Melhor estagiario do mundo
#     ''')




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Configurações do e-mail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'grodrigojunior@gmail.com'  # Substitua pelo seu e-mail
password = 'pjqp gnwz culg lzpo'            # Substitua pela sua senha

# Criar a mensagem
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'rjg_rodrigo@outlook.com'  # Substitua pelo e-mail do destinatário
msg['Subject'] = 'Relatório de Mercado'

# Corpo do e-mail
body = 'Olá, este é um e-mail enviado usando smtplib com anexos.'
msg.attach(MIMEText(body, 'plain'))

# Adicionar anexos
def attach_file(filename, mime_type):
    try:
        with open(filename, 'rb') as file:
            part = MIMEBase(*mime_type)
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(part)
            print(f'Anexo {filename} adicionado com sucesso.')
    except Exception as e:
        print(f'Erro ao anexar o arquivo {filename}: {e}')

# Adicione seus anexos
# attach_file('../graficos/AMBEV/ambev.png', ('image', 'png'))
# attach_file('../graficos/DOLAR/dolar.png', ('image', 'png'))


# Enviar o e-mail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Inicia a comunicação segura
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(username, msg['To'], text)
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar o e-mail: {e}')
finally:
    server.quit()
