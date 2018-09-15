# control of the cards
from lib.cvs import *
_metaclass_ = type


class Card:
    def __init__(self):
        self.crd = []  # the coordinate of the card (x, y)
        self.status = 0  # the status of the card "normal(0)" "restraint(1)" "resistance(2)"
        self.type = []  # type of the card "Quick(0)" "Arts(1)" "Buster(2)"
        self.priority = 0  # the priority of the card
        self.atk = 1  # set atk of the card

    def set_atk(self):
        if self.status == 1:
            self.atk = self.atk * 2
        elif self.status == 2:
            self.atk = self.atk * 0.5


def get_crd(sh, tmp, thd):  # get the coordinates of cards/marks
    ary = location(sh, tmp, thd)
    ary.sort()
    for i in range(len(ary)):
        for p in range(1, len(ary) - i):
            for k in range(-5, 5):
                for l in range(-5, 5):
                    if ((ary[i][0] + k) == ary[i + p][0]) and ((ary[i][1] + l) == ary[i + p][1]):
                        ary[i + p] = [0, 0]
    while ary.count([0, 0]) >= 1:
        ary.remove([0, 0])
    return ary


# This part is used to set the status of the cards
def get_restraint(sh):  # get the coordinates of the restraint mark
    threshold = 0.85
    restraint = get_crd(sh, 'res/restraint.png', threshold)
    return restraint


def get_resistance(sh):  # get the coordinates of the resistance mark
    threshold = 0.85
    resistance = get_crd(sh, 'res/resistance.png', threshold)
    return resistance


def mark_crd(card, mark, idk):  # get coordinates with certain marks
    note = []
    rxa = [i for i in range(150, 175)]
    rya = [i for i in range(260, 285)]
    rxb = [i for i in range(235, 260)]
    ryb = [i for i in range(295, 320)]
    rx = []
    ry = []

    if idk == 0:
        rx = rxa
        ry = rya
    elif idk == 1:
        rx = rxb
        ry = ryb

    for i in range(len(card)):
        for j in range(len(mark)):
            for p in rx:
                for q in ry:
                    if (card[i][0] + p == mark[j][0]) and (card[i][1] - q == mark[j][1]):
                        note.append(card[i])
    return note


def mark_restraint(card, mark):  # set the card's status
    for i in range(5):
        for j in range(len(mark)):
            if card[i].crd == mark[j]:
                card[i].status = 1


def mark_resistance(card, mark):  # set the card's status
    for i in range(5):
        for j in range(len(mark)):
            if card[i].crd == mark[j]:
                card[i].status = 2


# This part is used to set the type of the card
def set_type(cards, quick, arts, buster):
    for i in range(5):
        if quick != 0:
            for q in range(len(quick)):
                if cards[i].crd == quick[q]:
                    cards[i].type = 0
        if arts != 0:
            for a in range(len(arts)):
                if cards[i].crd == arts[a]:
                    cards[i].type = 1
        if buster != 0:
            for b in range(len(buster)):
                if cards[i].crd == buster[b]:
                    cards[i].type = 2
