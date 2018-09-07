# main method
from init import *
from anti import *
import time


def main():
    while screenshot():
        sh = screenshot()

        if check(sh, 'res/start.png', 0.9) == 1:
            pos = location(sh, 'res/start.png', 0.9)

            k = random.randrange(1, 3)
            for i in range(k):
                random_tap(sh)
                time.sleep(random.uniform(0.1, 1))

            tap_start(pos[0][0], pos[0][1])
            time.sleep(random.uniform(1, 2))

            cards = init_main(sh)

            time.sleep(random.uniform(0.1, 1))
            tap_card(cards[0][0], cards[0][1])
            time.sleep(random.uniform(0.1, 1))
            tap_card(cards[1][0], cards[1][1])
            time.sleep(random.uniform(0.1, 1))
            tap_card(cards[2][0], cards[2][1])

        if check(sh, 'res/end.png', 0.9) == 1:
            break


main()
