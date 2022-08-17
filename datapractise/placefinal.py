import json
import os
import requests

#Go into advanced system settings- set enviroment variable
#print(os.environ)


#-------------------------------OPEN FILE------------------------
with open("locations.json", "r") as f:
    data = json.load(f)
    #print(data.items())

print(data["places"])
#The list of dictionaires; each object has 3 keys and 3 values- makes it diffcult/ code consuming to acess the name and its X/Y values
places = [{'name': 'Edinburgh', 'x': 55.953251, 'y': -3.188267}, {'name': 'York', 'x': 53.958332, 'y': -1.080278}, 
{'name': 'Salford', 'x': 53.483002, 'y': -2.2931}, {'name': 'Perth', 'x': 56.396999, 'y': -3.437}, 
{'name': 'Newcastle', 'x': 54.966667, 'y': -1.6}, {'name': 'Dundee', 'x': 56.462002, 'y': -2.9707}, 
{'name': 'Liverpool', 'x': 53.400002, 'y': -2.983333}, {'name': 'Glasgow', 'x': 55.860916, 'y': -4.251433}, 
{'name': 'Oxford', 'x': 51.752022, 'y': -1.257677}, {'name': 'London', 'x': 51.509865, 'y': -0.118092}, 
{'name': 'Aberdeen', 'x': 57.149651, 'y': -2.099075}, {'name': 'Manchester', 'x': 53.483959, 'y': -2.244644}, 
{'name': 'Inverness', 'x': 57.477772, 'y': -4.224721}]

#New dictionary that will allow you to search for a city name as key- and return two values which are X/Y
places_dictitonary = {}
for place in places:
    places_dictitonary[place["name"].lower()] = { "latitude": place["x"], "logitude": place["y"] }


user_input_place = input("Enter place: ").lower()
#------------------------------ACESS LIST OF LIST-----------------
try:
    new_place = places_dictitonary[user_input_place]
except Exception:
    print("Place does not exist")
    exit(0)
print(new_place)

#------------------------------------GET REQUEST--------------------

#weather_data_of_json = requests.get(
   # f"https://api.openweathermap.org/data/2.5/weather?lat={}&lon={user_input_longitude}&appid={api_key}")

#data = json.loads(weather_data_of_json.text)
#print(data)

#print(weather_data_of_json.status_code)

# ctrl / comment out