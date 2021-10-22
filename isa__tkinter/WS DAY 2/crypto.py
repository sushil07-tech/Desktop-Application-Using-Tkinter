# pip install these -  requests, pillow
# create a random temp mail id for registering on api site - https://temp-mail.org/en/
# api site - https://coinlayer.com/signup/free
# api key on 21/08/2021 - f498ad2483bad1b04fd69eb0b390df89


# import requests
# from tkinter import *
# from datetime import datetime
# from PIL import Image, ImageTk

# def trackBitcoin():   #funtion to stalk creepy-crypto
#     url = "http://api.coinlayer.com/api/live?access_key=f498ad2483bad1b04fd69eb0b390df89&symbols=BTC,ETH,DOGE"

#     response = requests.get(url).json()
#     print(response["rates"])   # type - dictionary
   
#     BTCprice = response["rates"]["BTC"]
#     ETHprice = response["rates"]["ETH"]
#     DOGEprice = response["rates"]["DOGE"]
#     time = datetime.now().strftime("%H:%M:%S")

#     labelbtcprice.config(text = str(BTCprice) + " $")
#     labelethprice.config(text = str(ETHprice) + " $")
#     labeldogeprice.config(text = str(DOGEprice) + " $")
#     labeltime.config(text = "Updated at: " + time)

#     window.after(1000, trackBitcoin)

# window = Tk()
# window.geometry("400x400")
# window.title("Live Crypto tracker")
# window.config(background="misty rose")

# f1 = ("helvetica", 24, "bold")
# f2 = ("poppins", 22, "bold")
# f3 = ("poppins", 18, "bold italic")

# label = Label(window, text="LIVE TRACKER", font=f1, background="misty rose", foreground="blue4")
# label.place(x = 80, y = 40)

# labelbtcprice = Label(window, font=f2, background="misty rose", foreground="orange")
# labelbtcprice.place(x = 140, y = 130 )

# labelethprice = Label(window, font=f2, background="misty rose", foreground="black")
# labelethprice.place(x = 140, y =  190)

# labeldogeprice = Label(window, font=f2, background="misty rose", foreground="goldenrod3")
# labeldogeprice.place(x = 140, y =  250)

# labeltime = Label(window, font=f3, background="misty rose", foreground="dark blue")
# labeltime.place(x = 70, y = 340 )

# # IMAGES 
# image1 = Image.open("bitcoin.png")
# image1 = image1.resize((50,40), Image.ANTIALIAS)
# test = ImageTk.PhotoImage(image1)

# label1 = Label(image=test, background="misty rose")
# label1.image = test
# label1.place(x = 50, y = 130)

# image2 = Image.open("ethereum.png")
# image2 = image2.resize((50,40), Image.ANTIALIAS)
# test2 = ImageTk.PhotoImage(image2)

# label2 = Label(image=test2, background="misty rose")
# label2.image = test2
# label2.place(x = 50, y = 190)

# image3 = Image.open("dogecoin.png")
# image3 = image3.resize((50,40), Image.ANTIALIAS)
# test3 = ImageTk.PhotoImage(image3)

# label3 = Label(image=test3, background="misty rose")
# label3.image = test3
# label3.place(x = 50, y = 250)


# # # Restricting root window to change it's size according to user's need
# window.resizable(0, 0)

# # window.minsize(300, 200)   # Window shrunken to it’s minimum size (one cannot shrunk it any further)
  
# trackBitcoin()

# window.mainloop()