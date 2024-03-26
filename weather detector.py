from dotenv import load_dotenv
import datetime as dt
import sys
import requests
import os
choice = ['city', 'time', 'description', 'pressure', 'temperatures', 'humidity']

# load the environment variables
load_dotenv()
#To use env variables
# install python-dotenv using pip install python-dotenv
# create a .env file in the same directory as the script
# add the following line to the .env file
# API_KEY="the api key"


def get_weather_details(cityname):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = os.getenv("API_KEY")
    
    url = f"{base_url}q={cityname}&appid={api_key}"

    
    
    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin-273.1
        fahrenheit = (1.8*(kelvin-273)) + 32
        return celsius, fahrenheit

    response = requests.get(url)
    weather_data = response.json()
    
    if response.status_code == 200:
        # getting temperature
        wtemp_kelvin = weather_data['main']['temp']
        wtemp_celsius, wtemp_fahrenheit = kelvin_to_celsius_fahrenheit(wtemp_kelvin)

        # getting humidity
        whumidity = weather_data['main']['humidity']

        # getting weather description
        wdescription = weather_data['weather'][0]['description']

        # getting pressure
        wpressure = weather_data['main']['pressure']
    else:
        print('Error fetching weather data')
        sys.exit()
    return wpressure, whumidity, wtemp_celsius, wtemp_kelvin, wtemp_fahrenheit, wdescription

def user_input():
    user_choice = input("what will you like displayed within the list "
                    "\n[city,time,description,pressure,temperatures,humidity]: ").lower()
    return user_choice

#The variables city, pressure, humidity, description, temp_kelvin, temp_fahrenheit, and temp_celsius are used in the user_display function 
# but they are not defined within the function or passed as arguments. 
# This will cause a NameError if these variables are not defined in the global scope before the function is called.
# choice would have caused a NameError if it was not defined in the global scope before the function is called, but it is.
# Possible solution
def user_display(user_input, city, pressure, humidity, description, temp_kelvin, temp_fahrenheit, temp_celsius):
    userout = ""
    if user_input in choice or user_input == "temperature":
        if user_input == "city":
            userout = city
        elif user_input == "pressure":
            userout = f"{pressure} pa"
        elif user_input == "humidity":
            userout = f"{humidity} %"
        elif user_input == "description":
            userout = description
        elif user_input == "time":
            userout = dt.datetime.now()
        elif user_input == "temperatures" or user_input == "temperature":
            temp_unit = input("which units will you like temperature in [kelvin, fahrenheit, celsius]: ")
            if temp_unit == "kelvin":
                userout = f"{temp_kelvin} K"
            elif temp_unit == "fahrenheit":
                userout = f"{temp_fahrenheit} F"
            elif temp_unit == "celsius":
                userout = f"{temp_celsius}°C"
    else:
        userout = "please enter a value in the list"
    return userout


# main
while True:
    print('-'*75+"Welcome to the weather app"+'-'*75)
    city = input("Enter the name of the city: ")
    print()
    pressure, humidity, temp_celsius, temp_kelvin, temp_fahrenheit, description = get_weather_details(city)
    while True:
        user_choice = user_input()
        weather_data = user_display(user_choice,city,pressure,humidity,description,temp_kelvin,temp_fahrenheit,temp_celsius)
        print(f"{user_choice} : {weather_data}\n")
        attempt = input("will you need any other stuff: ").lower()
        if attempt == "no":
            break
    total_attempt = input("will you like to have a go at another city: ").lower()
    print()
    if total_attempt == "no":
        print("thank you for using this app")
        sys.exit()

