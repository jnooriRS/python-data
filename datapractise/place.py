import json
import os
import requests


#-------------------------------OPEN FILE------------------------
with open("locations.json", "r") as f:
    data = json.load(f)
    #print(data.items())

print(data["places"])
user_input_place = input("Enter place: ")
#------------------------------ACESS LIST OF LIST-----------------

#use filter() to find city name/ REMEMBER THIS IS A LIST OF DICTIRONARES/OBJECT- EACH OBJECT HAS THREE KEYS & VALUES
# try:
#raise exception if city does not exist
#print out lon/lat

#Then
#Default value
#------------------------------------GET REQUEST--------------------

#weather_data_of_json = requests.get(
   # f"https://api.openweathermap.org/data/2.5/weather?lat={}&lon={user_input_longitude}&appid={api_key}")

#data = json.loads(weather_data_of_json.text)
#print(data)

#print(weather_data_of_json.status_code)
#https://www.youtube.com/watch?v=4LsHsFPlzEE
# ctrl / comment out