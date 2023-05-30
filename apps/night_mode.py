"""nightmode app"""

# pylint: disable=import-error
# pylint: disable=no-name-in-module

import time
import ntptime
from constants import NIGHT_MODE_TIME


def is_night_mode():
    """checks whether the nightmode should be active or not"""
    try:
        ntptime.settime()
        local_time = time.localtime()
        local_hour = local_time[3]
        local_minute = local_time[4]

        local_hour = (local_hour + 2) % 24

        formated_time = float(f"{local_hour:02}.{local_minute:02}")

        if (
            formated_time > NIGHT_MODE_TIME["start"]
            or formated_time < NIGHT_MODE_TIME["end"]
        ):
            print("system in nightmode reducing brightness...")
            return True

        print("system in daymode increasing brightness...")
        return False

    # pylint: disable=broad-exception-caught
    except Exception:
        print("Did not work")
        return False
