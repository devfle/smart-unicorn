""""the clock app"""

# pylint: disable=import-error
import machine
import ntptime
import uasyncio
from utils import render_centered_text
from constants import BLACK, WIDTH, HEIGHT

# create the rtc object
rtc = machine.RTC()


# synchronize the RTC time from NTP
def sync_time() -> None:
    """syncs the current time"""
    try:
        ntptime.settime()
        print("Time set")
    except OSError:
        print("Error while trying to synch time!")


# function clearing the background
def clear_background(graphics) -> None:
    """removes all unnecessary pixels"""
    half_width = WIDTH // 2
    for x_val in range(0, half_width):
        graphics.set_pen(BLACK)
        for y_val in range(0, HEIGHT):
            graphics.pixel(x_val, y_val)
            graphics.pixel(WIDTH - x_val - 1, y_val)

    graphics.set_pen(BLACK)


_, _, _, _, _, minute, _, _ = rtc.datetime()

last_minute: int = minute
init_clock: bool = True


# Check whether the RTC time has changed and if so redraw the display
def redraw_display_if_reqd(graphics) -> None:
    """updates the time"""

    # pylint: disable=global-statement
    global minute, last_minute, init_clock

    _, _, _, _, hour, minute, _, _ = rtc.datetime()
    if minute != last_minute or init_clock:
        # "2" is the utc+2, maybe we have to fix this and add time
        hour = (hour + 2) % 24
        init_clock = False

        clear_background(graphics)
        message = f"{hour:02}:{minute:02}"

        render_centered_text(message, graphics)

        last_minute = minute


async def init(galactic, graphics):
    """inits the clock app"""

    # syncs the time from the server
    sync_time()

    while True:
        # updates the time
        redraw_display_if_reqd(graphics)

        # update the display
        galactic.update(graphics)

        # slow down loop
        await uasyncio.sleep(0.1)
