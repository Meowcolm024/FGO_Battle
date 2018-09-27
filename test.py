# used for testing
"""
get the coordinates of cards and marks
used to get the range for function mark_crd()
check whether the calculation is correct
change some parameters in "card.py" "anti.py" if necessary

Check line 37 and 38, annotate line 37 if you would like test the
image from your phone, if you only want to test local images,
annotate line 36 and set the directory of your image
"""
from init import *


def cards(sh):
    global quick, arts, buster
    threshold = 0.95
    quick = get_crd(sh, 'res/quick.png', threshold)
    arts = get_crd(sh, 'res/arts.png', threshold)
    buster = get_crd(sh, 'res/buster.png', threshold)

    all_cards = quick + arts + buster
    all_cards.sort()

    print("cards: ", all_cards)
    print("quick:", quick)
    print("arts: ", arts)
    print("buster: ", buster)


def marks(sh,):
    restraint = get_restraint(sh)
    resistance = get_resistance(sh)

    print("restraint: ", restraint)
    print("resistance: ", resistance)


def test():
    # sh = screenshot()
    sh = 'test/t1.jpeg'

    print('-------------')
    cards(sh)  # show coordinates of cards
    print('-------------')
    marks(sh)  # show coordinates of marks

    print('-------------')
    print("result: ", init_main(sh))  # show the result of calculation
    print('-------------')


test()
