# avoid the ID being banned
from lib.ats import *
from lib.cvs import *
import random


def long_tap(x, y):
    delay = random.uniform(0.01, 0.5)
    swipe(x, y, x, y, delay)


def tap_card(x, y):
    x0 = x + random.uniform(-100, 100)
    y0 = y + random.uniform(-20, 200)
    long_tap(x0, y0)


def tap_start(x, y):
    x0 = x + random.uniform(-75, 75)
    y0 = y + random.uniform(-75, 75)
    long_tap(x0, y0)


def random_tap(sh):
    if check(sh, 'res/start.png', 0.9) == 1:

        xa = random.uniform(300, 1000)
        ya = random.uniform(600, 750)
        xb = random.uniform(1200, 1500)
        yb = random.uniform(250, 450)

        if random.randrange(1, 2) == 1:
            long_tap(xa, ya)
        else:
            long_tap(xb, yb)

    if check(sh, 'res/quick.png', 0.9) == 1 \
            or check(sh, 'res/arts.png', 0.9) \
            or check(sh, 'res/buster.png', 0.9):

        x1 = random.uniform(1650, 1950)
        y1 = random.uniform(200, 500)
        x2 = random.uniform(200,500)
        y2 = random.uniform(180, 420)

        if random.randrange(1, 2) == 1:
            long_tap(x1, y1)
        else:
            long_tap(x2, y2)
