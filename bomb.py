from playsound import playsound
from time import sleep
from random import randrange


def boom(): playsound('boom.mp3')
def tick(): playsound('tick.mp3')

MIN_TIME = 10
MAX_TIME = 60
TICK_PER_SECOND = 1

TICK_LENGTH = 0.16

time_left = randrange(MIN_TIME, MAX_TIME + 1) * 1.0

sleep(1)

while time_left > 0:
    tick()
    time_left -= 1.0 / TICK_PER_SECOND
    sleep( max( 1.0 / TICK_PER_SECOND - TICK_LENGTH, 0 ) )
    if randrange(0, 10) == 1 and TICK_PER_SECOND < 5:
        TICK_PER_SECOND += 1

boom()