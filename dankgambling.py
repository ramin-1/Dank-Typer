from pynput.keyboard import Key, Controller
import time
import random
import math

keyboard = Controller()
time.sleep(5)


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def gamble():
    keyboard.type('pls bet 110k')
    enter()
    time.sleep(3)


def slots():
    keyboard.type('pls slots 100k')
    enter()
    time.sleep(3)


x = 0
while x < 1000000:
    # num = random.randint(1, 2)
    gamble()
    slots()
    # gamble()
    # time.sleep(3)
    # if num == 1:
    #    gamble()
    #    time.sleep(3)
    x += 1
