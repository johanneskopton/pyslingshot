# pylint: disable=import-error, no-name-in-module, unused-wildcard-import
from PyQt5.QtGui import QColor

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

SHIP_DISPLAY_SIZE = 30

PLAYER_COLORS = [QColor(50, 91, 168), QColor(50, 168, 82), QColor(191, 76, 65)]
PLAYER_NAMES = ["Blue", "Red"]


POWER_DISPLAY_FACTOR = 30
DEFAULT_POWER = 2

POWER_MAX = 4

KEY_ROTATION = 0.1
KEY_ROTATION_CONTROL = 0.02
KEY_POWER_STEP = 0.2
KEY_POWER_STEP_CONTROL = 0.04
GRAVITATION_CONSTANT = 12


TIMER_SPEED = 7
SPEED_FACTOR = 0.8

ZOOM_OUT_SCALE = 0.333

TIME_LIMIT = 3000


#WORLD GENERATION
N_SHIPS = 2

MIN_PLANETS = 2
MAX_PLANETS = 3

MIN_PLANET_SIZE = 50
MAX_PLANET_SIZE = 100

PLANET_PADDING = 30
PLANET_SHIP_PADDING = 80
SHIP_SHIP_PADDING = 300