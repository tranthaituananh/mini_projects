# Python program to find current weather details of any city using openweathermap api 
import requests 
from os import name, system

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

clear()

print("-" * 40, "Weather App", "-" * 40)
print("-" * 32, "Made by Tran Thai Tuan Anh", "-" * 33)

# Enter your API key here 
api_key = "a0aca8a89948154a4182dcecc780b513"
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

while(1):
    choice = int(input("\n1. Get weather by city name \n2. Exit \nEnter your choice: "))
    if choice == 1:
        # Give city name 
        city_name = input("Enter city name: ") 

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        response = requests.get(complete_url) 
        x = response.json() 

        if x["cod"] != "404": 
            y = x["main"] 
            current_temperature = y["temp"] - 273.15
            current_pressure = y["pressure"] 
            current_humidity = y["humidity"]
            z = x["weather"] 
            weather_description = z[0]["description"] 
            print(" → Temperature = " +
                            str(int(current_temperature)) + "°C" +
                "\n → Atmospheric pressure = " +
                            str(current_pressure) + " hPa" + 
                "\n → Humidity = " +
                            str(current_humidity) + " %" +
                "\n → Description = " +
                            str(weather_description)) 
        else: 
            print(" City Not Found ") 
    else:
        print("-" * 42,"Goodbye!", "-" * 41)
        exit()
