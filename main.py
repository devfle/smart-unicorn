"""The main file"""

# pylint: disable=import-error
# pylint: disable=no-name-in-module

import time
from secrets.wifi_config import SSID, WIFI_PW
import machine
import network
import uasyncio
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
from utils import render_centered_text, button_pressed, clear_display
from constants import BUTTON_MODE, SWITCH_APP_TIME, BRIGHTNESS, NIGHT_MODE_BRIGHTNESS
import apps.night_mode

# overclock to 200Mhz
machine.freq(200000000)

# create galactic object and graphics surface for drawing
galactic = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

# set display brightness
galactic.set_brightness(BRIGHTNESS)

# display boot text
render_centered_text("Loading...", graphics)
galactic.update(graphics)

# wait for better experience
time.sleep(5)

# connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, WIFI_PW)

WIFI_TIMER: int = 30
while WIFI_TIMER > 0:
    if wlan.isconnected() is True:
        print("successfull connected to wifi!")
        break

    WIFI_TIMER = WIFI_TIMER - 1
    time.sleep(1)

if wlan.isconnected() is False:
    print("connection to your wifi failed! Init soft reset")
    clear_display(galactic, graphics)
    render_centered_text("Error 1", graphics)
    galactic.update(graphics)
    time.sleep(5)

    # soft reset because without wifi connection the apps would not work
    machine.soft_reset()


async def enqueue_app(init_app):
    """starts and stops the apps"""
    try:
        await uasyncio.wait_for(init_app(galactic, graphics), timeout=SWITCH_APP_TIME)
    # pylint: disable=broad-exception-caught
    except Exception:
        clear_display(galactic, graphics)
        is_night_mode: bool = apps.night_mode.is_night_mode()

        if is_night_mode is True:
            galactic.set_brightness(NIGHT_MODE_BRIGHTNESS)
        else:
            galactic.set_brightness(BRIGHTNESS)

        print("switching to next app...")


# wait for a button to be pressed and load that effect
if BUTTON_MODE is True:
    while True:
        if button_pressed(galactic) == GalacticUnicorn.SWITCH_A:
            import apps.clock_app

            break
        if button_pressed(galactic) == GalacticUnicorn.SWITCH_B:
            import apps.weather_app

            break
else:
    try:
        import apps.clock_app
        import apps.weather_app
    # pylint: disable=broad-exception-caught
    except Exception:
        print("error while importing")

    while True:
        # for first run, have to improve this
        clear_display(galactic, graphics)
        print("starting weather app...")
        uasyncio.run(enqueue_app(apps.weather_app.init))

        print("starting clock app...")
        uasyncio.run(enqueue_app(apps.clock_app.init))
