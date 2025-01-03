import requests 
from plyer import notification 


CITY = "Череповец"
KEY_API = "23496c2a58b99648af590ee8a29c5348"


def get_weather(city: str = CITY, api_key: str = KEY_API)-> dict:
    """
    Выполняет запрос к API и возвращает данные о погоде в виде словаря.
    """
    url = rf'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()


def format_weather_message(weather_dict: dict) -> str:

    """
    Получает данные из функции get_weather и форматирует их в удобочитаемое сообщение
    """

    # температура
    temp = weather_dict['main']['temp']
    # ощущение температуры
    feels_like = weather_dict['main']['feels_like']
    # что на улице
    description =weather_dict['weather'][0]['description']

    return (f"температура: {temp}, ощущается как: {feels_like}, описание: {description}")


def notify_weather(message: str) -> None:
    
    """
    Уведомление
    """
    notification.notify(
    title = f"Погода в {CITY}",
    message = message,
    app_name = 'Weather',
    app_icon = None
    )


def main() -> None:
    # долго немог понять откуда берутся данные в предидущих функциях, но теперь всё встало на места когда увидел что мы их передаём через функцию main()
    weather_dict = get_weather()
    message = format_weather_message(weather_dict)
    notify_weather(message)



if __name__ == "__main__":
    main()   