# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# link in internet 
#http://www.codeskulptor.org/#user5-3Ntjs1RwwB-2.py
#import simplegui
import random
import math
# initialize global variables used in your code
rangeMax = 100
secretNumber = 0

# define event handlers for control panel
    
def range100():
    global rangeMax
    rangeMax = 100
    # button that changes range to range [0,100) and restarts

def range1000():
    # button that changes range to range [0,1000) and restarts
    global rangeMax
    rangeMax = 1000 
       
def get_input(guess):
    # main game logic goes here    
    global secretNumber
    print secretNumber
    guess = int (guess)
    if guess < secretNumber:
        print 'Higher !'
        return False
    elif guess > secretNumber:
        print 'Lower'
        return False
    else:
        return True
    
def init():
    global rangeMax, secretNumber
    test = False
    guessesLeft = 10
    secretNumber = random.randrange(rangeMax)
    while guessesLeft > 0:
        print 'I guesed number bitween 0 and ',rangeMax
        guess = raw_input('Enter your number: ')
        test = get_input(guess)
        if not test:
            guessesLeft -= 1
        else:
            break
    if guessesLeft >= 0:
        print 'SUCCESS!!!'
    else:
         print 'FAIL!!!'
        
# create frame


# register event handlers for control elements
init()

# start frame


# always remember to check your completed program against the grading rubric
