"""constants for application"""

# pylint: disable=import-error
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN
from galactic import GalacticUnicorn

# create a PicoGraphics framebuffer to draw into
graphics = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN)

# pen colors to draw with
WHITE = graphics.create_pen(255, 255, 255)
YELLOW = graphics.create_pen(230, 230, 0)
BLUE = graphics.create_pen(0, 0, 210)
BLACK = graphics.create_pen(0, 0, 0)

# time in seconds to switch to the next app
SWITCH_APP_TIME = 300

# display brightness
BRIGHTNESS = 0.25

# button mode
BUTTON_MODE = False

# height and width information
WIDTH: int = GalacticUnicorn.WIDTH
HEIGHT: int = GalacticUnicorn.HEIGHT

# night mode config
NIGHT_MODE_BRIGHTNESS = 0.10
NIGHT_MODE_TIME = {"start": 23.00, "end": 8.00}
