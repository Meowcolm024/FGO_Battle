# avoid the ID being banned
from lib.ats import *
import random


def tap_card(x, y):
    x0 = x + random.uniform(-100, 100)
    y0 = y + random.uniform(-20, 200)
    tap(x0, y0)
