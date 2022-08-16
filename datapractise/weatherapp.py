
import requests
import json
import os
#API for Open Weather
#env file

user_input_latitude = input("Enter latitude: ")
user_input_longitude = input("Enter longitude: ")

#Check user inpt
print(user_input_latitude)
print(user_input_longitude)

#Content type header- set to json in POSTMAN if inputting manually

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={user_input_latitude}&lon={user_input_longitude}&appid={api_key}")

data = json.loads(weather_data.text)
print(data)

print(weather_data.status_code)

