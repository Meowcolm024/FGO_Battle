# initialize and calculate the best combination
from card import *


def init():  # initialize 5 command cards
    a = Card()
    b = Card()
    c = Card()
    d = Card()
    e = Card()
    global cards
    cards = [a, b, c, d, e]
    return cards


def init_cards(sh):
    global quick, arts, buster
    threshold = 0.95
    quick = get_crd(sh, 'res/quick.png', threshold)
    arts = get_crd(sh, 'res/arts.png', threshold)
    buster = get_crd(sh, 'res/buster.png', threshold)

    all_cards = quick + arts + buster
    all_cards.sort()

    for i in range(len(all_cards)):
        cards[i].crd = all_cards[i]

    return all_cards


def init_status(sh, cards_crd):
    restraint = mark_crd(cards_crd, get_restraint(sh), 0)
    resistance = mark_crd(cards_crd, get_resistance(sh), 1)

    mark_restraint(cards, restraint)
    mark_resistance(cards, resistance)


def rank_card():
    atk = [0, 0, 0]
    total = 0
    rank = [0, 0, 0]

    for i in range(5):
        cards[i].get_atk()

    for i in range(5):
        cards[i].priority = 1
        for j in range(5):
            if j == i:
                continue
            else:
                cards[j].priority = 2
                for k in range(5):
                    if k == i or k == j:
                        continue
                    else:
                        if cards[i].type == 2:
                            atk[0] = 2 * cards[i].atk
                            if cards[j].type == 2:
                                atk[1] = 2.3 * cards[j].atk
                            elif cards[j].type == 1:
                                atk[1] = 1.7 * cards[j].atk
                            elif cards[j].type == 0:
                                atk[1] = 1.46 * cards[j].atk

                            if cards[k].type == 2:
                                atk[2] = 2.6 * cards[k].atk
                            elif cards[k].type == 1:
                                atk[2] = 1.9 * cards[k].atk
                            elif cards[k].type == 0:
                                atk[2] = 1.62 * cards[k].atk
                        else:
                            if cards[i].type == 1:
                                atk[0] = 1 * cards[i].atk
                            elif cards[i].type == 0:
                                atk[0] = 0.8 * cards[i].atk

                            if cards[j].type == 2:  # buster
                                atk[1] = 1.8 * cards[j].atk
                            elif cards[j].type == 1:  # arts
                                atk[1] = 1.2 * cards[j].atk
                            elif cards[j].type == 0:  # quick
                                atk[1] = 0.96 * cards[j].atk

                            if cards[k].type == 2:
                                atk[2] = 2.1 * cards[k].atk
                            elif cards[k].type == 1:
                                atk[2] = 1.4 * cards[k].atk
                            elif cards[k].type == 0:
                                atk[2] = 1.12 * cards[k].atk

                    if (sum(atk)) > total:
                        total = sum(atk)
                        rank[0] = i
                        rank[1] = j
                        rank[2] = k

    return rank


def init_main(sh):
    init()
    cards_crd = init_cards(sh)
    init_status(sh, cards_crd)
    set_type(cards, quick, arts, buster)

    final = rank_card()

    return final


# only for testing
def main():
    sh = 'test/t2.jpeg'
    print(init_main(sh))


main()
