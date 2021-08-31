# <--imports-->
import time
import requests
import tkinter as tk

# define weather api 
def getWeather(astro):
      city = textfield.get()
      api = "http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=9eb2a3f199c1fce2d9638830c7d1c7ae"
      json_data = requests.get(api).json()
      condition = json_data['weather'][0]['main']
      temp = int(json_data['main']['temp'] - 273.15)
      min_temp = int(json_data['main']['temp_min'] - 273.15)
      max_temp = int(json_data['main']['temp_max'] - 273.15)
      pressure = json_data['main']['pressure']
      hum = json_data['main']['humidty']
      wind = json_data['wind']['speed']
      
      final_info = condition + "\n" + str(temp) + "°C"
      final_data = "\n" + "Max Temp:" + str(max_temp) + "\n" + "Min Temp:" + str(min_temp) + "\n" + "Pressure:" + str(pressure) + "\n" + "Wind:" + str(wind) + "\n" "Humidity:" + str(hum)
      
      label1.config(text = final_info)
      label2.config(text = final_data)
      
# INTERFACE
astro = tk.Tk()
astro.geometry("300x200")
astro.title("ASTRO-WEATHER-APP")

f = ("poppins", 15, "bold")
t = ("poppins", 25, "bold")

textfield = tk.Entry(astro, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<return>', getWeather)
label1 = tk.Label(astro, font = t)
label1.pack()
label2 = tk.Label(astro, font = f)
label2.pack()


astro.mainloop()
