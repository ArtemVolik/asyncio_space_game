import time
import curses
import random
from animation.background import blink
from animation.ship_1 import ship
from pathlib import Path


TIC_TIMEOUT = 0.1


with open(Path('animation/frame1.txt'), 'r') as file:
    frame1 = file.read()

with open(Path('animation/frame2.txt'), 'r') as file:
    frame2 = file.read()


def draw(canvas):

    curses.curs_set(False)
    canvas.nodelay(True)

    y, x = canvas.getmaxyx()

    coroutines = [
        blink(canvas,
              random.randrange(0, y),
              random.randrange(0, x),
              random.choice('+*.:')
              )
        for _ in range(100)
    ]

    ship_frames = ship(canvas, frame1, frame2, y, x)

    while True:

        for coroutine in coroutines.copy():
            try:
                for i in range(random.randint(1, 4)):

                    coroutine.send(None)

            except StopIteration:
                coroutines.remove(coroutine)
            if len(coroutines) == 0:
                break

        ship_frames.send(None)

        canvas.refresh()
        time.sleep(0.15)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
