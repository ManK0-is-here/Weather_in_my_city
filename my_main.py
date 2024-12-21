from urllib import response
import requests 
from plyer import notification 

CITY = "Череповец"
KEY_API = "23496c2a58b99648af590ee8a29c5348"

def get_weather(city: str = CITY, api_key: str = KEY_API)-> dict:
    url = rf'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response: Response = requests.get(url)
    return requests.json()