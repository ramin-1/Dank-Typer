from pynput.keyboard import Key, Controller
import time
import random
import math

keyboard = Controller()
time.sleep(5)


def beg():
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 5))


def gamble():
    keyboard.type('pls gamble 100')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 5))


def slots():
    keyboard.type('pls slots 100')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 5))


def cookie():
    keyboard.type('pls sell cookie')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 5))


def pm():
    keyboard.type('pls pm')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(1, 3))
    num = random.randint(1, 4)
    if num == 1:
        keyboard.press('r')
        keyboard.release('r')
    elif num == 2:
        keyboard.press('d')
        keyboard.release('d')
    elif num == 3:
        keyboard.press('n')
        keyboard.release('n')
    else:
        keyboard.press('e')
        keyboard.release('e')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(2, 5))


phrases = ["damn", "coolio", "im rich af", "oop", "shiii", "dam it", "cmon man", "lol", "ripp",
           "wtf", "crazy stuff", "gimme more coin", "bruh", "lmao", "what thee heck", "haha", "good bot", 
           "xd","what do you want man?","wow","bad bot","rip the laptop","wow","why u doin this","grinding is tough man"]


def phrase():
    phrase_num = random.randint(0, (len(phrases)-1))
    keyboard.type(phrases[phrase_num])
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


x = 0
cook_buy = random.randint(240, 260)
while x < 1000000:
    num = random.randint(1, 7)
    if num == 1:
        cookie()
        slots()
        cookie()
        gamble()
        cookie()
        pm()
        cookie()
        beg()
        cookie()
    elif num == 2:
        cookie()
        gamble()
        cookie()
        slots()
        cookie()
        pm()
        cookie()
        beg()
        cookie()
    elif num == 3:
        pm()
        cookie()
        gamble()
        cookie()
        beg()
        cookie()
        slots()
        cookie()
    elif num == 4:
        slots()
        cookie()
        pm()
        cookie()
        gamble()
        cookie()
        beg()
        cookie()
    elif num == 5:
        cookie()
        pm()
        cookie()
        beg()
        cookie()
        slots()
        gamble()
        cookie()
    elif num == 6:
        cookie()
        pm()
        cookie()
        slots()
        beg()
        cookie()
        gamble()
        cookie()
    else:
        cookie()
        beg()
        slots()
        cookie()
        pm()
        cookie()
        gamble()
        cookie()
    if x == cook_buy:
        cookie_num = random.randint(240, 260)
        keyboard.type(f'pls buy cookie {cookie_num}')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        cook_buy += random.randint(240, 260)
    phrase()
    time.sleep(random.randint(7, 12))
    x += 1

"""
#words = ["pls beg", "pls slots 100", "pls gamble 100"]
x = 0
while x < 1000000:
    num = random.randint(1,6)
    if num == 1:
        keyboard.type('pls beg')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls slots 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls gamble 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))  
        keyboard.type('pls pm')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(5,10))   
    elif num == 2:
        keyboard.type('pls slots 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls beg')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls pm')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(5,10))
        keyboard.type('pls gamble 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
    elif num ==3:
        keyboard.type('pls gamble 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls pm')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(5,10))
        keyboard.type('pls slots 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls beg')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
    elif num == 4:
        keyboard.type('pls pm')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(5,10))
        keyboard.type('pls gamble 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls beg')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls slots 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
    elif num == 5:
        keyboard.type('pls beg')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls pm')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(5,10))
        keyboard.type('pls slots 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls gamble 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
    else:
        keyboard.type('pls gamble 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls slots 100')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
        keyboard.type('pls pm')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(5,10))
        keyboard.type('pls beg')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(2,5))
    time.sleep(random.randint(7, 12))
    x += 1
"""


#curry2 = lambda h: lambda x: lambda y: h(x,y)
"""
prev0, prev1 = 0, 0
    while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            if feral_hogs:
                if abs(num_rolls - prev0) == 2:
                    score0 += 3
                prev0 = take_turn(num_rolls, score1, dice)
                score0 += prev0
            else: 
                score0 += take_turn(num_rolls, score1, dice)
            if is_swap(score0, score1):
                score0, score1 = score1, score0
        else:
            num_rolls = strategy1(score1, score0)
            if feral_hogs:
                if abs(num_rolls - prev1) == 2:
                    score1 += 3
                prev0 = take_turn(num_rolls, score0, dice)
                score1 += prev1
            else:
                score1 += take_turn(num_rolls, score0, dice)
            if is_swap(score1, score0):
                score0, score1 = score1, score0
        who = other(who)
        say = say(score0, score1)
    return score0, score1 
"""
