import json, websocket, pprint, talib, numpy, slack, os
from pathlib import Path
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *


SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_4h"
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) #carrega a token do bot
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

#Informação RSI
RSI_PERIOD = 6
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

closes = []
in_position = True

def on_open(ws):
    print('conexão aberta')
    client.chat_postMessage(channel='#btc-4hr', text="Sinalizador-bot entrou em operação, RSI de 6 períodos ")

def on_close(ws):
    print('conexão fechada')

def on_message(ws, message):
    global closes, in_position
    print('mensagem recebida')
    json_message = json.loads(message)
    pprint.pprint(json_message)
    candle = json_message['k']

    is_candle_closed = candle['x']
    close = float(candle['c'])

    if is_candle_closed:
        print("candle fechado em {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all sri calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                print("Sobrecomprado! Vender!")
                client.chat_postMessage(channel='#btc-4hr',
                                        text=":botão_up: O RSI está sobrecomprado, bom momento para short"
                                             ", RSI: {:.2f}, preço ${:.2f}, RSI de 6 períodos  :botão_up: ".format(last_rsi,close))
                in_position = True
            if last_rsi < RSI_OVERSOLD:
                print("Oversold! Buy! Buy! Buy!")
                client.chat_postMessage(channel='#btc-4hr',
                                        text=":seta_para_baixo: O RSI está sobrevendido, bom momento para long"
                                             ", RSI:{:.2f}, preço = ${:.2f}, RSI de 6 períodos  :seta_para_baixo:".format(last_rsi,close))
                in_position = True
            if RSI_OVERSOLD < last_rsi and RSI_OVERBOUGHT > last_rsi:
                if in_position:
                    print("RSI ENTROU EM ZONA NEUTRA")
                    client.chat_postMessage(channel='#btc-4hr', text="O indicador RSI entrou em zona neutra"
                                                                       ", RSI:{:.2f}, Preço = ${:.2f}, RSI de 6 períodos ".format(last_rsi,close))
                    in_position = False
                else:
                    print("bot ok")

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close= on_close, on_message=on_message)

ws.run_forever()