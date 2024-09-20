import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os

#https://www.treinaweb.com.br/blog/enviando-email-com-python-e-smtp

def SendMail(Retorno_Ibovespa : str, Retorno_Dolar : str, Retorno_SeP500 : str):
    # Configurações do e-mail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    username = 'YourMail' 
    password = 'AppKey_Google_Acconunt'
    recipient = "recipient_email"


    # Retorno_Ibovespa = '1%'
    # Retorno_Dolar = '1%'
    # Retorno_SeP500 = '1%'


    # Criar a mensagem
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = 'Relatório de Mercado'

    bodyMail = f'''
                    Preazado diretor, segue o relatório de mercado: 
                    
                    * O Ibovespa teve o retorno de {Retorno_Ibovespa}
                    * O Dólar teve o retorno de {Retorno_Dolar}
                    * O S&P500 teve o retorno de {Retorno_SeP500}

                    segue em anexo a performance dos ativos nos últimos 6 meses


                    att, 
                    Melhor estagiario do mundo

                '''


    msg.attach(MIMEText(bodyMail, 'plain'))

    #Anexar imagem - Deveria fazer um For para todas as pastas de graficos
    image_path = 'graficos/ibovespa/ibovespa.png'
    with open(image_path, 'rb') as img:
        img_data = img.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        msg.attach(image)

    image_path = 'graficos/dolar/dolar.png'
    with open(image_path, 'rb') as img:
        img_data = img.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        msg.attach(image)

    image_path = 'graficos/s&p500/s&p500.png'
    with open(image_path, 'rb') as img:
        img_data = img.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        msg.attach(image)

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(username, password)

        server.sendmail(
        username,
        recipient,
        msg.as_string())
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')
    finally:
        server.quit()

    # for Mail in recipient:
    #     try:
            
    #         server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    #         server.login(username, password)

    #         server.sendmail(
    #         username,
    #         Mail,
    #         msg.as_string())
    #         print("Email enviado com sucesso!")

    #     except Exception as e:
    #         print(f'Erro ao enviar o e-mail: {e}')
    #     finally:
    #         server.quit()



# server.send_message(
#     msg.as_string(),
#     username,
#     recipient
# )


# try:
#     server = smtplib.SMTP_SSL(smtp_server, smtp_port)
#     server.starttls() #Iniciar conexão segura
#     server.login(username, password)

#     text = msg.as_string()
#     server.sendmail(username, msg['To'], text)
#     print('E-mail enviado com sucesso!')
# except Exception as e:
#     print(f'Erro ao enviar o e-mail: {e}')
# finally:
#     server.quit()



#=====================================================
# import smtplib

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login("grodrigojunior@gmail.com", "pjqp gnwz culg lzpo")

# server.sendmail(
#   "grodrigojunior@gmail.com",
#   "newway.interactive@gmail.com",
#   "Email Teste")
# server.quit()