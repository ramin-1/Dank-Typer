from pynput.keyboard import Key, Controller
import time
import random
import math

keyboard = Controller()
time.sleep(5)

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def beg():
    keyboard.type('pls beg')
    enter()
    time.sleep(random.randint(2, 5))


def gamble():
    keyboard.type('pls gamble 100')
    enter()
    time.sleep(random.randint(2, 5))


def slots():
    keyboard.type('pls slots 100')
    enter()
    time.sleep(random.randint(2, 5))


def cookie():
    keyboard.type('pls sell cookie')
    enter()
    time.sleep(random.randint(2, 5))
    
def buy():
    keyboard.type('pls buy cookie')
    enter()
    time.sleep(random.randint(2, 5))

def trivia():
    keyboard.type('pls trivia')
    enter()
    time.sleep(random.randint(1, 2))
    trivia_num = random.randint(1,4)
    if trivia_num == 1:
        keyboard.type('A')
    elif trivia_num == 2:
        keyboard.type('B')
    elif trivia_num == 3:
        keyboard.type('C')
    else: 
        keyboard.type('D')
    enter()
    time.sleep(random.randint(2, 5))

def use():
    keyboard.type('pls use cookie')
    enter()
    time.sleep(random.randint(2, 5))

def scout():
    keyboard.type('pls scout')
    enter()
    time.sleep(random.randint(1, 2))
    keyboard.type('tree')
    enter()
    time.sleep(random.randint(2, 5))

def pm():
    keyboard.type('pls pm')
    enter()
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
    enter()
    time.sleep(random.randint(2, 5))

def full_cookie():
    cookie()
    use()
    buy()
    time.sleep(random.randint(1, 2))


phrases = ["damn", "coolio", "im rich af", "oop", "shiii", "dam it", "cmon man", "lol", "ripp",
           "wtf", "crazy stuff", "gimme more coin", "bruh", "lmao", "what thee heck", "haha", "good bot", 
           "xd","what do you want man?","wow","bad bot","rip the laptop","wow","why u doin this","grinding is tough man"]


def phrase():
    phrase_num = random.randint(0, (len(phrases)-1))
    keyboard.type(phrases[phrase_num])
    enter()


x = 0
cook_buy = random.randint(90, 110)
while x < 1000000:
    num = random.randint(1, 7)
    if num == 1:
        use()
        trivia()
        cookie()
        slots()
        scout()
        slots()
        gamble()
        cookie()
        pm()
        buy()
        beg()
        use()
    elif num == 2:
        trivia()
        use()
        gamble()
        buy()
        slots()
        use()
        scout()
        cookie()
        pm()
        buy()
        beg()
        use()
    elif num == 3:
        slots()
        pm()
        trivia()
        cookie()
        gamble()
        buy()
        scout()
        beg()
        use()
        slots()
        buy()
    elif num == 4:
        gamble()
        scout()
        buy()
        slots()
        cookie()
        pm()
        buy()
        gamble()
        use()
        trivia()
        cookie()
        beg()
        buy()
    elif num == 5:
        cookie()
        use()
        scout()
        cookie()
        pm()
        buy()
        beg()
        trivia()
        cookie()
        slots()
        buy()
        gamble()
        buy()
    elif num == 6:
        buy()
        pm()
        cookie()
        slots()
        gamble()
        trivia()
        beg()
        buy()
        scout()
        use()
        gamble()
        cookie()
    else:
        cookie()
        beg()
        scout()
        use()
        slots()
        buy()
        pm()
        use()
        trivia()
        cookie()
        gamble()
        buy()
    if x == cook_buy:
        cookie_num = random.randint(340, 360)
        keyboard.type(f'pls buy cookie {cookie_num}')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        cook_buy += random.randint(90, 110)
    phrase()
    time.sleep(random.randint(2, 5))
    x += 1
    
#No Selling
