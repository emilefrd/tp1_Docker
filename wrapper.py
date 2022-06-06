import requests
import os
from dotenv import load_dotenv


load_dotenv()

APIKEY = os.environ['APIKEY'] #get key 
X = os.environ['LONG']  #get longitude
Y = os.environ['LAT']  #get latitude


getter = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + Y + "&lon=" + X + "&appid=" + APIKEY + "&units=metric")


print(getter.status_code)
print(getter.json())
