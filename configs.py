# Change the game settings here!
# Available colors:
from curses import (COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN,
                    COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW)


# Board size:
LINES = 12
COLUMNS = 12

# Snake configs:
SNAKE_CHAR = "O"
SNAKE_COLOR = COLOR_GREEN
INITIAL_SIZE = 2

# Apple appearance:
APPLE_CHAR = "*"
APPLE_COLOR = COLOR_RED

# Empty coordinate appearance:
EMPTY_CHAR = "'"
EMPTY_COLOR = COLOR_WHITE

# Text appearance:
TEXT_COLOR = COLOR_YELLOW

# Game pacing:
REFRESH_TIME = 0.11 # seconds
