# Welcome to Smart Unicorn

Smart Unicorn is an micro-python based firmware based on the [Pimoroni-Pico firmware](https://github.com/pimoroni/pimoroni-pico) for the [Galactic Unicorn rgb matrix display](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/galactic_unicorn#about-galactic-unicorn).

Theoretically, this firmware should also work on other matrix displays with a few adjustments. However, I have not tried this yet. If someone has tested this, I appreciate your feedback.

The firmware is currently still at alpha stage. I am always happy to receive feedback and support.

## Features

- Wifi integration
- Clock app
- Night-Mode app
- Live Weather app
- Configurable and automatic app switch

## Currently in Todo

- Webserver
- Setup page
- Config page
- Next train / bus app
- Current date app

## Setup

Currently there is no complete bundle and the [Pimoroni-Pico firmware](https://github.com/pimoroni/pimoroni-pico) still has to be installed on its own. I will optimize this in the future.
After installing the base firmware, this project must be checked out and then transferred to the Raspberry Pi Pico.

Afterwards, a secrets folder must be created in the root directory:
```bash
mkdir secrets
```

### Weather App Setup

Create the needed config file
```bash
touch secrets/weather_config.py
```

Add the following constants to the ```weather_config.py```
```python
LAT: float = YOUR_LAT_VALUE
LON: float = YOUR_LON_VALUE
```

### WIFI Setup

Create the needed config file
```bash
touch secrets/wifi_config.py
```

Add the following constants to the ```wifi_config.py```
```python
SSID: str = "YOUR_SSID"
WIFI_PW: str = "YOUR_WIFI_PW"
```

<b>NOTE: Without an active internet connection this firmware does not work at the moment.</b>

## Configuration

Some functions of this firmware can be customized like the display brightness. Currently the variables for this are in the [constants.py](https://github.com/devfle/smart-unicorn/blob/main/constants.py).

## Error Codes

This firmware uses error codes to inform you about an error. This list contains all available error codes with an explanation of the error:

| Code    | Explanation |
| :--------: | :-------: |
| Error 1  | wifi connection failed |



