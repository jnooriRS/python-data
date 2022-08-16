import requests
import json
import os

lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, {os.getenv('api_key')})

response = requests.get(url)
data = json.loads(response.text)
print(data)