# main method
from init import *
from anti import *
import time


def main():
    while screenshot():
        time.sleep(random.uniform(0.75, 1.5))
        sh = screenshot()
        # check if battle is ready start
        if check(sh, 'res/start.png', 0.9) == 1:
            pos = location(sh, 'res/start.png', 0.9)
            # random tap
            k = random.randrange(0, 2)
            for i in range(k):
                random_tap(sh)
                time.sleep(random.uniform(0.1, 0.3))
            # tap the "attack" button
            tap_start(pos[0][0], pos[0][1])
        # if at the card-selecting interface
        if check(sh, 'res/quick.png', 0.9) == 1 \
                or check(sh, 'res/arts.png', 0.9) \
                or check(sh, 'res/buster.png', 0.9):
            # random tap
            j = random.randrange(0, 2)
            for i in range(j):
                random_tap(sh)
                time.sleep(random.uniform(0.1, 0.3))
            # select cards
            cards = init_main(sh)
            # tap selected cards
            time.sleep(random.uniform(0.1, 0.4))
            tap_card(cards[0][0], cards[0][1])
            time.sleep(random.uniform(0.1, 0.4))
            tap_card(cards[1][0], cards[1][1])
            time.sleep(random.uniform(0.1, 0.4))
            tap_card(cards[2][0], cards[2][1])
        # check if the battle ends
        if check(sh, 'res/end.png', 0.9) == 1:
            break


main()
