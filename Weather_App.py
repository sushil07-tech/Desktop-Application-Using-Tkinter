import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import requests



from configparser import ConfigParser

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini' 
config1 = ConfigParser()
config1.read(config_file)
api_key = config1['api_key']['key']

#Fetching Data from the API

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        icons = json["weather"][0]["icon"]
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        humidity = json['main']['humidity']
        weather = json['weather'][0]['main']
        dicreption = json['weather'][0]['description']
        sunrise = time.strftime("%H:%M:%S", time.gmtime(json['sys']['sunrise'] + 19800))
        sunset = time.strftime("%H:%M:%S", time.gmtime(json['sys']['sunset'] + 19800))
        final = (city, country, icons, temp_celsius, temp_fahrenheit,humidity, weather, dicreption, sunrise, sunset)
        return final
    else:
        return None

def search():
    global img
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img['file'] = 'weathericon/{}.png'.format(weather[2])
        temp_lbl['text'] = '{:.2f}°C | {:.2f}°F,  Humidity = {}%'.format(weather[3], weather[4],weather[5])
        weather_lbl['text'] = weather[6]
        dicreption_lbl['text'] = 'Condition : {}'.format(weather[7])
        sunrise_lbl['text'] = 'Sunrise Time: {}'.format(weather[8])
        sunset_lbl['text'] = 'Sunset Time: {}'.format(weather[9])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Wheather App")
app.geometry('600x300')

#setting Background
app.configure(background="#b3ffff")

#Setting the icon For the app
p1 = PhotoImage(file = 'weathericon/icon.png')
app.iconphoto(False, p1)

#setting up icon for app window
search_icon = Image.open("weathericon/search.png")
search_icon = search_icon.resize((30,30),Image.ANTIALIAS) 
search_icon = ImageTk.PhotoImage(search_icon)

#setting up the logo of app
image1 = Image.open("weathericon/Logo.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x= 0, y= 0, anchor=NW )

#title bar
title_lbl = Label(app, text="Search city name", font=('Bold', 15),bg = "#660066",foreground="#ffccff",anchor=W, padx=30)
title_lbl.place(x=149.5,y=0, width=460, height=50)

#creating search box to search the city name
city_text = StringVar()
city_entry = Entry(app, textvariable= city_text)
city_entry.place(x=370, y=15)

#creating the search button
search_btn = Button(app,cursor="hand2",bd = 0,image = search_icon , width=40, command=search, bg = "#660066",activebackground=  "#660066")
search_btn.place(x=500, y=10)

#location label
location_lbl = Label(app, text='', font=('Comic Sans MS', 20),bg="#b3ffff")
location_lbl.place(x=200, y =80)

#image label to show the weather condition
img = PhotoImage(file= "")
Image = Label(app, image = img, bg="#b3ffff")
Image.place(x=20,y=65)

#temperature Label to display tempareture
temp_lbl = Label(app, text='', font=('Comic Sans MS', 15),bg="#b3ffff")
temp_lbl.place(x=200, y=120)

#label to print the weather condition
weather_lbl = Label(app, text='', font=('Comic Sans MS', 20),bg="#b3ffff")
weather_lbl.place(x=40,y=195)

#label to print the Discription of the weather
dicreption_lbl = Label(app, text='',font=('Comic Sans MS', 16),bg="#b3ffff")
dicreption_lbl.place(x=200,y=150)

#for printing sunrise time
sunrise_lbl = Label(app, text='',font=('Comic Sans MS',16),bg="#b3ffff")
sunrise_lbl.place(x=200,y=180)

#for printing sunset time
sunset_lbl = Label(app, text='',font=('Comic Sans MS',16),bg="#b3ffff")
sunset_lbl.place(x=200,y=210)

#footer of our website
footer_lbl = Label(app, text='Developed by Sushil kori D11B',background="#660066")
footer_lbl.place(x=0,y=270,relwidth=1,height=30)
app.mainloop()
