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
    time.sleep(random.randint(2, 3))


def gamble():
    keyboard.type('pls bet 1.5k')
    enter()
    time.sleep(random.randint(2, 3))


def slots():
    keyboard.type('pls slots 1.5k')
    enter()
    time.sleep(random.randint(2, 3))
    
def sell():
    keyboard.type('pls use pet')
    enter()
    time.sleep(random.randint(2, 3))

def cookie():
    # keyboard.type('pls use cheese')
    # enter()
    # time.sleep(random.randint(1, 2))
    # keyboard.type('y')
    # enter()
    # time.sleep(random.randint(2, 3))
    x = random.randint(1, 2)
    if x == 1:
        use()
    else:
        buy()


def buy():
    keyboard.type('pls buy coo')
    enter()
    time.sleep(random.randint(2, 3))


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
    time.sleep(random.randint(2, 3))


def use():
    # keyboard.type('pls use pink')
    # enter()
    # time.sleep(random.randint(1, 2))
    # keyboard.type('myself')
    # enter()
    # time.sleep(random.randint(2, 4))
    keyboard.type('pls use pet')
    enter()
    time.sleep(random.randint(2, 3))


def scout():
    keyboard.type('pls scout')
    enter()
    time.sleep(random.randint(1, 2))
    keyboard.type('air')
    enter()
    time.sleep(random.randint(2, 3))


def pm():
    keyboard.type('pls pm')
    enter()
    time.sleep(random.randint(1, 2))
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
           "xd", "what do you want man?", "wow", "bad bot", "rip the laptop", "wow", "why u doin this",
           "grinding is tough man"]


def phrase():
    phrase_num = random.randint(0, (len(phrases) - 1))
    keyboard.type(phrases[phrase_num])
    enter()


def bank():
    keyboard.type('pls use ban')
    enter()
    time.sleep(3)


def cookies():
    keyboard.type('pls sell k')
    enter()
    time.sleep(3)


def pink():
    keyboard.type('pls use pink')
    enter()
    time.sleep(3)


def badBoy():
    keyboard.type('/temprole <@327520551776026625> Bad Boy 1m')
    enter()
    time.sleep(3)

def shortBadBoy():
    keyboard.type('/temprole <@327520551776026625> Bad Boy 7s')
    enter()
    time.sleep(3)


def banknotes():
    x = 0
    num = random.randint(1, 4)
    while x < 1000000:
        if num == 1:
            bank()
            cookies()
            pink()
        elif num == 2:
            cookies()
            pink()
            bank()
        elif num == 3:
            bank()
            pink()
            cookies()
        elif num == 4:
            pink()
            bank()
            cookies()
    x += 1


def freexp():
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
        if x == cook_buy:
            cook_buy += random.randint(90, 110)
            badBoy()
        #     keyboard.type(f'pls buy cookie {cookie_num}')
        #     keyboard.press(Key.enter)
        #     keyboard.release(Key.enter)
        #     cook_buy += random.randint(90, 110)
        phrase()
        time.sleep(random.randint(1, 2))
        x += 1
        
def fishGrind():
    x = 0
    cook_buy = random.randint(90, 110)
    lag_number = random.randint(10, 15)
    while x < 1000000:
        sell()
        slots()
        gamble()
        x += 1
        if x == lag_number:
            lag_number += random.randint(10, 15)
           # shortBadBoy()
            
        if x == cook_buy:
                cook_buy += random.randint(90, 110)
              #  badBoy()    
    
    


# This is where the stuff runs
fishGrind()
#freexp()
# banknotes()

# No Selling

# x = 0
# while x < 1000000:
#     num = random.randint(1, 7)
#     if num == 1:
#         trivia()
#         use()
#         pm()
#         beg()
#         scout()
#     elif num == 2:
#         trivia()
#         use()
#         scout()
#         beg()
#         pm()
#     elif num == 3:
#         scout()
#         trivia()
#         pm()
#         use()
#         beg()
#     elif num == 4:
#         use()
#         scout()
#         trivia()
#         beg()
#         pm()
#     elif num == 5:
#         scout()
#         use()
#         pm()
#         trivia()
#         beg()
#     elif num == 6:
#         beg()
#         scout()
#         trivia()
#         pm()
#         use()
#     else:
#         use()
#         beg()
#         scout()
#         trivia()
#         pm()

#     phrase()
#     time.sleep(random.randint(4,7))
#     x += 1

# No Gamble/Scout
# cook_buy = random.randint(90, 110)
# while x < 1000000:
#     num = random.randint(1, 7)
#     if num == 1:
#         use()
#         trivia()
#         cookie()
#         #slots()
#         use()
#         scout()
#         #slots()
#         buy()
#         #gamble()
#         use()
#         pm()
#         buy()
#         cookie()
#         beg()
#         use()
#     elif num == 2:
#         use()
#         trivia()
#         use()
#         #gamble()
#         buy()
#         #slots()
#         cookie()
#         use()
#         scout()
#         cookie()
#         pm()
#         buy()
#         beg()
#         use()
#     elif num == 3:
#         use()
#         #slots()
#         cookie()
#         pm()
#         buy()
#         trivia()
#         cookie()
#         #gamble()
#         buy()
#         scout()
#         use()
#         beg()
#         use()
#         #slots()
#         buy()
#     elif num == 4:
#         #gamble()
#         scout()
#         buy()
#         #slots()
#         cookie()
#         pm()
#         buy()
#         #gamble()
#         use()
#         trivia()
#         cookie()
#         beg()
#         #gamble()
#     elif num == 5:
#         buy()
#         cookie()
#         use()
#         scout()
#         cookie()
#         pm()
#         use()
#         #slots()
#         beg()
#         buy()
#         cookie()
#         trivia()
#         use()
#         #slots()
#         buy()
#         #gamble()
#         buy()
#     elif num == 6:
#         buy()
#         pm()
#         cookie()
#         #slots()
#         use()
#         #gamble()
#         cookie()
#         trivia()
#         buy()
#         beg()
#         buy()
#         scout()
#         use()
#         #gamble()
#         use()
#     else:
#         cookie()
#         beg()
#         use()
#         scout()
#         use()
#         #slots()
#         buy()
#         pm()
#         use()
#         trivia()
#         use()
#         #gamble()
#         buy()
#     if x == cook_buy:
#         cookie_num = random.randint(340, 360)
#         keyboard.type(f'pls buy cookie {cookie_num}')
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         cook_buy += random.randint(90, 110)
#     phrase()
#     time.sleep(random.randint(1,3))
#     x += 1
