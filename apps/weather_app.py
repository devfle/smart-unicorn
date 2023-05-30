"""the weather app"""

# pylint: disable=import-error
# pylint: disable=no-name-in-module

from secrets.weather_config import LAT, LON
import uasyncio
import urequests
from utils import generate_weather_icon, render_centered_text

host: str = "https://api.brightsky.dev/"
option: str = "current_weather"


def get_current_weather(lat: float, lon: float) -> dict or None:
    """retrieves weather data"""

    if lat is None or lon is None:
        return None

    # define query params
    query = f"?lat={lat}&lon={lon}"

    # retrieve data from weather api
    weather_data = urequests.request("GET", f"{host}{option}{query}")
    weather_data_dict = weather_data.json()

    # extract the temperature data
    temperature: int = round(weather_data_dict["weather"]["temperature"], 1)
    icon: str = weather_data_dict["weather"]["icon"]

    weather_data.close()

    return {"temperature": temperature, "icon": icon}


async def init(galactic, graphics):
    """inits weather app"""
    while True:
        print("fetching weather data...")

        # get weather data and create message
        current_weather: dict = get_current_weather(LAT, LON)
        message: str = f"{current_weather['temperature']}°"

        # render the message
        render_centered_text(message, graphics)

        # render the icon
        icon = current_weather["icon"]

        if icon in ["clear-day", "clear-night"]:
            generate_weather_icon("sun", graphics)
        elif icon in ["cloudy", "fog"]:
            generate_weather_icon("cloud", graphics)
        elif icon in ["partly-cloudy-day", "partly-cloudy-night"]:
            generate_weather_icon("sun", graphics)
        elif icon in ["rain", "wind"]:
            generate_weather_icon("rain", graphics)
        elif icon in ["snow", "hail", "sleet"]:
            generate_weather_icon("rain", graphics)
        elif icon == "thunderstorm":
            generate_weather_icon("rain", graphics)
        else:
            generate_weather_icon("sun", graphics)

        # update the display
        galactic.update(graphics)

        # wait 2.5 min to next api request
        await uasyncio.sleep(150)
