import requests
import os
from dotenv import load_dotenv


load_dotenv()
APIKEY = os.environ['APIKEY']
X = os.environ['LONG']  
Y = os.environ['LAT']  


getter = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + Y + "&lon=" + X + "&appid=" + APIKEY + "&units=metric")


print(getter.status_code)
print(getter.json())