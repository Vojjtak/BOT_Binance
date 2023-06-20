from binance import Client
from api import API, SCR_KEY
import functions as fc
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login system")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

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





