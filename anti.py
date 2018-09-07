# avoid the ID being banned
from lib.ats import *
from lib.cvs import *
import random


def long_tap(x, y):  # random length tap
    delay = random.randrange(5, 300)
    swipe(x, y, x, y, delay)


def tap_card(x, y):  # tap on random location of the card
    x0 = x + random.uniform(0, 100)
    y0 = y + random.uniform(-150, 0)
    x0 = int(x0)
    y0 = int(y0)
    tap(x0, y0)


def tap_start(x, y):  # tap on random location of the button
    x0 = x + random.uniform(0, 50)
    y0 = y + random.uniform(-50, 0)
    x0 = int(x0)
    y0 = int(y0)
    tap(x0, y0)


def random_tap(sh):  # random tap on the screen
    if check(sh, 'res/start.png', 0.75) == 1:

        x0 = random.randrange(1200, 1500)
        y0 = random.randrange(250, 450)
        long_tap(x0, y0)

    if check(sh, 'res/quick.png', 0.9) == 1 \
            or check(sh, 'res/arts.png', 0.9) \
            or check(sh, 'res/buster.png', 0.9):

        x1 = random.randrange(1200, 1800)
        y1 = random.randrange(200, 500)

        long_tap(x1, y1)

