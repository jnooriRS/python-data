# OPENWEATHER 44ad1f7ca09faba5a87f676c8565dcde
import requests
#API for Open Weather
api_key = 

user_input_latitude = input("Enter latitude: ")
user_input_longitude = input("Enter longitude: ")

#Check user inpt
#print(user_input_latitude)
#print(user_input_longitude)


weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={user_input_latitude}&lon={user_input_longitude}&appid={api_key}"
)
print(weather_data.status_code)
