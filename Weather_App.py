from tkinter import*
from tkinter import messagebox
from types import resolve_bases
import requests



from configparser import ConfigParser

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini' 
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        humidity = json['main']['humidity']
        weather = json['weather'][0]['main']
        dicreption = json['weather'][0]['description']
        final = (city, country, temp_celsius, temp_fahrenheit,humidity, weather, dicreption)
        return final
    else:
        return None



def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F, Humidity = {}%'.format(weather[2], weather[3],weather[4])
        weather_lbl['text'] = weather[5]
        dicreption_lbl['text'] = weather[6]
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Wheather App")
app.geometry('700x300')


title_lbl = Label(app, text="Weather App using Tkinter", font=('bold', 20))
title_lbl.pack()

city_text = StringVar()
city_entry = Entry(app, textvariable= city_text)
city_entry.pack()


search_btn = Button(app, text='Search Weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()


temp_lbl = Label(app, text='',font=('bold', 15))
temp_lbl.pack()

weather_lbl = Label(app, text='',font=('bold', 14))
weather_lbl.pack()

dicreption_lbl = Label(app, text='',font=(13))
dicreption_lbl.pack()

app.mainloop()