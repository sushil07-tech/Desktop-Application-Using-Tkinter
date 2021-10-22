import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():   #funtion to stalk creepycrypto
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR"
    response = requests.get(url).json()
    print(response)   # type - dictionary
    BTCprice = response["BTC"]["USD"]
    ETHprice = response["ETH"]["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelbtcprice.config(text = str(BTCprice) + "$")
    labelethprice.config(text = str(ETHprice) + "$")
    labeltime.config(text = "Updated at: " + time)

    canvas.after(1000, trackBitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin tracker")
canvas.config(background="misty rose")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="Bitcoin price", font=f1)
label.pack(pady=20)

labelbtcprice = tk.Label(canvas, font=f2)
labelbtcprice.pack(pady=20)

labelethprice = tk.Label(canvas, font=f2)
labelethprice.pack(pady=20)

labeltime = tk.Label(canvas, font=f3)
labeltime.pack(pady=20)

trackBitcoin()

canvas.mainloop()