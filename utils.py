"""util functions"""

# pylint: disable=import-error
from galactic import GalacticUnicorn
from constants import WHITE, YELLOW, BLUE, BLACK


def clear_display(galactic, graphics):
    """clears the display"""
    graphics.set_pen(BLACK)
    graphics.clear()
    galactic.update(graphics)


def render_centered_text(message: str, graphics):
    """renders an centered text"""

    # set text color
    graphics.set_pen(WHITE)

    # set the font
    graphics.set_font("bitmap8")

    # calc to center the text
    width: int = GalacticUnicorn.WIDTH
    w_val: int = graphics.measure_text(message, 1)
    x_val: int = int(width / 2 - w_val / 2 + 1)

    # render the text
    graphics.text(message, x_val, 2, scale=1)


# returns the id of the button that is currently pressed
def button_pressed(galactic):
    """detects button press"""

    if galactic.is_pressed(GalacticUnicorn.SWITCH_A):
        return GalacticUnicorn.SWITCH_A
    if galactic.is_pressed(GalacticUnicorn.SWITCH_B):
        return GalacticUnicorn.SWITCH_B
    if galactic.is_pressed(GalacticUnicorn.SWITCH_C):
        return GalacticUnicorn.SWITCH_C
    if galactic.is_pressed(GalacticUnicorn.SWITCH_D):
        return GalacticUnicorn.SWITCH_D
    return None

# pylint: disable=too-many-statements
# we have to find better option then using pixel method
def generate_weather_icon(icon: str, graphics):
    """generates the icon for the current weather"""

    if icon == "sun":
        # set pixel color
        graphics.set_pen(YELLOW)

        graphics.rectangle(3, 3, 5, 5)
        graphics.pixel(3, 1)
        graphics.pixel(1, 3)
        graphics.pixel(1, 7)
        graphics.pixel(7, 1)
        graphics.pixel(3, 9)
        graphics.pixel(7, 9)
        graphics.pixel(9, 3)
        graphics.pixel(9, 7)

    elif icon == "rain":
        # set pixel color
        graphics.set_pen(WHITE)

        graphics.pixel(1, 4)
        graphics.pixel(2, 3)
        graphics.pixel(2, 4)
        graphics.pixel(2, 5)
        graphics.pixel(3, 2)
        graphics.pixel(3, 3)
        graphics.pixel(3, 4)
        graphics.pixel(3, 5)
        graphics.pixel(3, 6)
        graphics.pixel(4, 3)
        graphics.pixel(4, 4)
        graphics.pixel(4, 5)
        graphics.pixel(5, 4)
        graphics.pixel(6, 3)
        graphics.pixel(6, 4)
        graphics.pixel(6, 5)
        graphics.pixel(7, 2)
        graphics.pixel(7, 3)
        graphics.pixel(7, 4)
        graphics.pixel(7, 5)
        graphics.pixel(7, 6)
        graphics.pixel(8, 3)
        graphics.pixel(8, 4)
        graphics.pixel(8, 5)
        graphics.pixel(9, 4)

        graphics.pixel(2, 2)
        graphics.pixel(2, 6)
        graphics.pixel(3, 1)
        graphics.pixel(3, 7)
        graphics.pixel(4, 2)
        graphics.pixel(4, 6)
        graphics.pixel(5, 3)
        graphics.pixel(5, 5)
        graphics.pixel(6, 2)
        graphics.pixel(6, 6)
        graphics.pixel(7, 1)
        graphics.pixel(7, 7)
        graphics.pixel(8, 2)
        graphics.pixel(8, 6)

        # set pixel color
        graphics.set_pen(BLUE)

        graphics.pixel(4, 7)
        graphics.pixel(5, 8)
        graphics.pixel(6, 9)
        graphics.pixel(8, 7)
        graphics.pixel(9, 8)
        graphics.pixel(10, 9)

    elif icon == "cloud":
        # set pixel color
        graphics.set_pen(WHITE)

        graphics.pixel(1, 5)
        graphics.pixel(2, 4)
        graphics.pixel(2, 5)
        graphics.pixel(2, 6)
        graphics.pixel(3, 3)
        graphics.pixel(3, 4)
        graphics.pixel(3, 5)
        graphics.pixel(3, 6)
        graphics.pixel(3, 7)
        graphics.pixel(4, 4)
        graphics.pixel(4, 5)
        graphics.pixel(4, 6)
        graphics.pixel(5, 5)
        graphics.pixel(6, 4)
        graphics.pixel(6, 5)
        graphics.pixel(6, 6)
        graphics.pixel(7, 3)
        graphics.pixel(7, 4)
        graphics.pixel(7, 5)
        graphics.pixel(7, 6)
        graphics.pixel(7, 7)
        graphics.pixel(8, 4)
        graphics.pixel(8, 5)
        graphics.pixel(8, 6)
        graphics.pixel(9, 5)

        graphics.pixel(2, 3)
        graphics.pixel(2, 7)
        graphics.pixel(3, 2)
        graphics.pixel(3, 8)
        graphics.pixel(4, 3)
        graphics.pixel(4, 7)
        graphics.pixel(5, 4)
        graphics.pixel(5, 6)
        graphics.pixel(6, 3)
        graphics.pixel(6, 7)
        graphics.pixel(7, 2)
        graphics.pixel(7, 8)
        graphics.pixel(8, 3)
        graphics.pixel(8, 7)
