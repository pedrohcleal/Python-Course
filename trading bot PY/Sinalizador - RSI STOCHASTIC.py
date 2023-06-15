import json, websocket, pprint, talib, numpy, slack, os
from pathlib import Path
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *


SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)  #carrega a token do bot
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

#Informação RSI

RSI_OVERBOUGHT = 80
RSI_OVERSOLD = 20
RSI_PERIOD = 14

closes = []
in_position = True

def on_open(ws):
    print('conexão aberta')
    client.chat_postMessage(channel='#btc-rsi_stock-1min', text="bot entrou em teste")

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
            fastk, fastd = talib.STOCHRSI(np_closes, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
            print("all rsi calculated so far")
            print(fastk, fastd)
            last_rsi = fastk
            print("the current rsi {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                print("Sobrecomprado! Vender!")
                client.chat_postMessage(channel='#btc-rsi_stock-1min', text=":seta_para_baixo: :círculo_vermelho_preenchido: O STOCH RSI está sobrecomprado, bom momento para short :seta_para_baixo: "
                                                                            ":círculo_vermelho_preenchido: RSI: {}, preço ${} :botão_up: ".format(last_rsi, close))
                in_position= True
            if last_rsi < RSI_OVERSOLD:
                print("Oversold! Buy! Buy! Buy!")
                client.chat_postMessage(channel='#btc-rsi_stock-1min', text=":botão_up: :círculo_verde_grande: O STOCH RSI está sobrevendido, bom momento para long :botão_up: "
                                                                            ":círculo_verde_grande: RSI: {}, preço ${} :botão_up: ".format(last_rsi, close))
                in_position = True
            if RSI_OVERSOLD < last_rsi and RSI_OVERBOUGHT > last_rsi:
                if in_position:
                    print("RSI ENTROU EM ZONA NEUTRA")
                    client.chat_postMessage(channel='#btc-rsi_stock-1min', text="O indicador STOCH RSI entrou em zona neutra RSI: {}, preço ${} :botão_up: ".format(last_rsi, close))
                    in_position = False
                else: print("bot ok")

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close= on_close, on_message=on_message)

ws.run_forever()