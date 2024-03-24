import datetime as dt
import sys
import requests
choice = ['city', 'time', 'description', 'pressure', 'temperatures', 'humidity']


def get_weather_details(cityname):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key="0a54022a5462b135185573cb0f224107"
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
    usercho = input("what will you like displayed within the list "
                    "\n[city,time,description,pressure,temperatures,humidity]").lower()
    return usercho


def user_display(userinput):
    if userinput in choice or userinput == "temperature":
        if userinput == "city":
            userout = city
        elif userinput == "pressure":
            userout = f"{pressure} pa"
        elif userinput == "humidity":
            userout = f"{humidity} %"
        elif userinput == "description":
            userout = description
        elif userinput == "time":
            userout = dt.datetime.now()
        elif userinput == "temperatures" or userinput == "temperature":
            temp_unit = input("which units will you like temperature in [kelvin, fahrenheit, celsius]")
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
    print('-'*70+"Welcome to the weather app"+'-'*79)
    city = input("Enter the name of the city ")
    print()
    pressure, humidity, temp_celsius, temp_kelvin, temp_fahrenheit, description = get_weather_details(city)
    while True:
        userc = user_input()
        weather_data = user_display(userc)
        print(f"{userc} : {weather_data}\n")
        attempt = input("will you need any other stuff").lower()
        if attempt == "no":
            break
    total_attempt = input("will you like to have a go at another city").lower()
    print()
    if total_attempt == "no":
        print("thank you for using this app")
        sys.exit()

