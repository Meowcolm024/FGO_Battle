# get the coordinates of cards and marks
# used to get the range for function mark_crd()
from card import *


def cards(sh):
    global quick, arts, buster
    threshold = 0.95
    quick = get_crd(sh, 'res/quick.png', threshold)
    arts = get_crd(sh, 'res/arts.png', threshold)
    buster = get_crd(sh, 'res/buster.png', threshold)

    all_cards = quick + arts + buster
    all_cards.sort()

    print("cards: ", all_cards)


def marks(sh,):
    restraint = get_restraint(sh)
    resistance = get_resistance(sh)

    print("restraint: ", restraint)
    print("resistance: ", resistance)


def test():
    sh = 'test/t4.jpeg'

    cards(sh)
    marks(sh)


test()
