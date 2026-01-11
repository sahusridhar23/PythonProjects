import requests
import json
import win32com.client as wincom

print("Welcome to WeatherApp 1.0 .Created by Sridhar Sahu\n")

while True:
    try :
        city = input("Enter the city name:")
        if city.lower() == 'exit':
            print("Thank you for using WeatherApp 1.0")
            speak = wincom.Dispatch("SAPI.SpVoice")
            speak.speak("Thank you for using WeatherApp 1.0")
            break
        url = f"https://api.weatherapi.com/v1/current.json?key=d71e9e5a9b8345e8a4622336261101&q={city}"
        r = requests.get(url)
        # print(type(r.text)) - json string

        wdic = json.loads(r.text) #parse json string to dictionary
        w = wdic["current"]["temp_c"]
        print('temp_C = ',w)
        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.speak(f"Temprature in {city} is {w} degree celcius" )
    except:
        print("invalid city name, Please enter a valid city name")


