from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
from api import API, SCR_KEY
from binance.enums import *
import json
import requests

symbol = "DOGEUSDT"
quantity = 100
client = Client(API, SCR_KEY)
def getdata(symbol):
    """Get data from binance
    Choose symbol, timeframe"""
    client = Client(API, SCR_KEY)
    symbol = "DOGEUSDT"
    frame = pd.DataFrame(client.get_historical_klines(symbol, "1m", "200 minutes UTC"))
    frame = frame.iloc[:, 0:5]
    frame.columns = ["Time", "Open", "High", "Low", "Close"]
    frame.set_index("Time", inplace=True)
    frame.index = pd.to_datetime(frame.index, unit="ms")
    frame = frame.astype(float)
    return frame


def indicator(df):
    """Indicator when bot should place buy order"""
    buy = True
    price_list = []
    for price in df.iloc[194:198]["Open"]:
        price_list.append(price)
        if any(price_list) < df.iloc[199]["Open"]:
            buy = True
        else:
            buy = False
    return buy
    


def buy(buy):
    """Buy or not
    This function is placing an final buy order"""
    client = Client(API, SCR_KEY)
    symbol = "DOGEUSDT"
    if buy:
        client.create_test_order(symbol=symbol, side=SIDE_BUY, type=ORDER_TYPE_MARKET, quantity=quantity)
        print("Accepted trade.")
        return
    else:
        print("Indicator doesnt allow to buy.")
        return


def current_price(symbol):
    """Get a current price of any symbol"""
    KEY_TO_CURRENT_PRICE = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    current_price = requests.get(KEY_TO_CURRENT_PRICE)
    current_price = current_price.json()
    current_price = current_price["price"]
    return current_price


def sell(df, current_price):
    """Sell order if a price will be above 110% of open-price"""
    open_price = (df.iloc[199]["Open"])
    percentage = float(open_price)/100
    #Missing navigation to specific order
    if current_price >= percentage*110:
        client.create_test_order(symbol=symbol, side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity=quantity)
        print(f"You sold {quantity} of {symbol}")
        return
