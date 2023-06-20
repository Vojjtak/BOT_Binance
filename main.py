from binance import Client
from api import API, SCR_KEY
import functions as fc


# Base
client = Client(API, SCR_KEY)
investment = 1
symbol = "DOGEUSDT"

# dataframe of symbol stores in rows
df = fc.getdata(symbol)

# action when to place order
buy = fc.indicator(df)
# current symbol/coin price
current_price = float(fc.current_price(symbol))
# buy_price
open_price = float(df.iloc[199]["Open"])
# if current_price = 110% buy_price = sell
fc.sell(df, current_price)





