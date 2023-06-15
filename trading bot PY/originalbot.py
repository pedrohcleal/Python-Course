import json, websocket, pprint, talib, numpy, config

from binance.client import Client
from binance.enums import *

#OFICIAL

SOCKET = "wss://stream.binance.com:9443/ws/bnbbusd@kline_1m"

RSI_PERIOD = 14
RSI_OVERRBOUGHT = 65
RSI_OVERSOLD = 35
TRADE_SYMBOL = 'BNBBUSD'
TRADE_QUANTITY = 10.1

closes = []
in_position = False

ultimo_preco = 100000000

client = Client(config.API_KEY, config.API_SECRET, tld='us')

#RETIRAR "#" DA LINHA ABAIXO PARA FUNCIONAR !

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False
    return True

def on_open(ws):
    print('conexão aberta')

def on_close(ws):
    print('conexão fechada')

def on_message(ws, message):
    global closes, in_position
    print('mensagem recebida')
    json_message = json.loads(message)
    pprint.pprint(json_message)
    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

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

            if last_rsi > RSI_OVERRBOUGHT:
                if in_position and candle['c'] > ultimo_preco:
                    print("sell! sell! sell!")
                    #put binance sell logic here
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    ultimo_preco = candle['c']
                    if order_succeeded:
                        in_position = False
                else:
                    print("está comprado demais, não fazer nada ")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("está sobrevendido, não há nada pra fazer aqui")
                else:
                    if candle['c'] < ultimo_preco:
                        print("buy! buy ! buy!")
                        #put binance oder logic here
                        order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True
                        ultimo_preco = candle['c']

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close= on_close, on_message=on_message)

ws.run_forever()