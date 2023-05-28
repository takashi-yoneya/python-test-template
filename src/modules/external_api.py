import typing as t

import requests


def get_weather(city_code: int) -> dict[str, t.Any]:
    URL = f"https://weather.tsukumijima.net/api/forecast/city/{city_code}"
    res = requests.get(URL)
    return res.json()
