import requests, os, boto3
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

aws_access_key_id = os.getenv('amazon_access_key_id')
aws_secret_access_key = os.getenv('amazon_secret_access_key')
num_mandar = os.getenv('num_mandar')
correo_mandar = os.getenv('correo_mandar')

ses = boto3.client('ses', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")

senders = os.getenv('senders')

def enviar_mensaje(mensaje):

    req=requests.post(senders+"/whatsapp/send_message",json={"message":mensaje,"phone_number":num_mandar,"display_phone_number":"+1(415)682-6034"})

def enviar_correo(mensaje,monto):

    response = ses.send_email(
        Source="matiasttt222@gmail.com",
        Destination={
            "ToAddresses": [correo_mandar]
        },
        Message={
            "Subject": {"Data": f"Insiders data <{monto}>"},
            "Body": {
                "Text": {"Data": mensaje}
            }
        }
    )