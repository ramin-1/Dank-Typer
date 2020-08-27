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
    time.sleep(random.randint(2, 4))


def gamble():
    keyboard.type('pls bet 100')
    enter()
    time.sleep(random.randint(1, 3))


def slots():
    keyboard.type('pls slots 100')
    enter()
    time.sleep(random.randint(1, 3))


def cookie():
    use()


def buy():
    keyboard.type('pls buy coo')
    enter()
    time.sleep(random.randint(2, 4))


def trivia():
    keyboard.type('pls trivia')
    enter()
    time.sleep(random.randint(1, 2))
    trivia_num = random.randint(1, 4)
    if trivia_num == 1:
        keyboard.type('A')
    elif trivia_num == 2:
        keyboard.type('B')
    elif trivia_num == 3:
        keyboard.type('C')
    else:
        keyboard.type('D')
    enter()
    time.sleep(random.randint(2, 4))


def use():
    keyboard.type('pls use pink')
    enter()
    time.sleep(random.randint(1, 2))
    keyboard.type('g')
    enter()
    time.sleep(random.randint(2, 4))


def scout():
    keyboard.type('pls scout')
    enter()
    time.sleep(random.randint(1, 2))
    keyboard.type('air')
    enter()
    time.sleep(random.randint(2, 4))


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
    time.sleep(random.randint(3, 5))


def full_cookie():
    cookie()
    use()
    buy()
    time.sleep(random.randint(1, 2))


phrases = ["damn", "coolio", "im rich af", "oop", "shiii", "dam it", "cmon man", "lol", "ripp",
           "wtf", "crazy stuff", "gimme more coin", "bruh", "lmao", "what thee heck", "haha", "good bot",
           "xd", "what do you want man?", "wow", "bad bot", "rip the laptop", "wow", "why u doin this", "grinding is tough man"]


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
        # slots()
        use()
        scout()
        # slots()
        buy()
        # gamble()
        use()
        pm()
        buy()
        cookie()
        beg()
        use()
    elif num == 2:
        use()
        trivia()
        use()
        # gamble()
        buy()
        # slots()
        cookie()
        use()
        scout()
        cookie()
        pm()
        buy()
        beg()
        use()
    elif num == 3:
        use()
        # slots()
        cookie()
        pm()
        buy()
        trivia()
        cookie()
        # gamble()
        buy()
        scout()
        use()
        beg()
        use()
        # slots()
        buy()
    elif num == 4:
        # gamble()
        scout()
        buy()
        # slots()
        cookie()
        pm()
        buy()
        # gamble()
        use()
        trivia()
        cookie()
        beg()
        # gamble()
    elif num == 5:
        buy()
        cookie()
        use()
        scout()
        cookie()
        pm()
        use()
        # slots()
        beg()
        buy()
        cookie()
        trivia()
        use()
        # slots()
        buy()
        # gamble()
        buy()
    elif num == 6:
        buy()
        pm()
        cookie()
        # slots()
        use()
        # gamble()
        cookie()
        trivia()
        buy()
        beg()
        buy()
        scout()
        use()
        # gamble()
        use()
    else:
        cookie()
        beg()
        use()
        scout()
        use()
        # slots()
        buy()
        pm()
        use()
        trivia()
        use()
        # gamble()
        buy()
    # if x == cook_buy:
    #     cookie_num = random.randint(340, 360)
    #     keyboard.type(f'pls buy cookie {cookie_num}')
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)
    #     cook_buy += random.randint(90, 110)
    phrase()
    time.sleep(random.randint(1, 3))
    x += 1
    
#No Selling
