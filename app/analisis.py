import requests
import pandas as pd
from datetime import datetime, timezone
from app.dynamo_functions import read, write
from app.senders import enviar_mensaje, enviar_correo

def main():

    print("INICIANDO...")

    lectura = read()

    hora_ultima = datetime.fromisoformat(lectura["valor"])

    req=requests.get("https://wallettrackapi-655880131780.us-central1.run.app/")

    data=req.json()

    max_fecha=hora_ultima

    for i in data["data"]:

        monto_total = i["size"]*i["price"]
        evento_titulo = i["eventSlug"]
        evento_especifico = i["slug"]
        proxy_wallet = i["proxyWallet"]
        avg_entry_price = i["avg_entry_price"]
        outcome = i["outcome"]
        user_profit_loss = i["user_profit_loss"]
        total_trades = i["total_trades"]

        timestamp = datetime.fromtimestamp(i['timestamp'], tz=timezone.utc)
        max_fecha = max(timestamp,hora_ultima)

        if(monto_total>5000 and avg_entry_price<0.9 and (hora_ultima<timestamp)):
        
            print(evento_titulo,monto_total,timestamp,"vs",hora_ultima)

            profile=f"https://polymarket.com/profile/{proxy_wallet}"

            mensaje=f"Evento: {evento_titulo}\nEspecifico: {evento_especifico}\nMonto: {monto_total}\nLado: {outcome}\nPrice: {avg_entry_price}\nPnL: {user_profit_loss}\nNum trades: {total_trades}\nCuenta: {profile}"

            enviar_correo(mensaje,monto_total)

    write(max_fecha.isoformat())


        