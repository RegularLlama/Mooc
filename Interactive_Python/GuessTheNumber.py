# http://www.codeskulptor.org/#user41_iL28XZYo2z_3.py
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "Started new game"
    global secret
    secret = None
    # remove this when you add your code
    global counter
    counter = 0

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret
    secret = random.randrange(0, 100)
    global count
    count = int(math.ceil(math.log(100+1,2)))
    global counter
    counter = 0

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret
    secret = random.randrange(0, 1000)
    global count
    count = int(math.ceil(math.log(1000+1,2)))
    global counter
    counter = 0

def input_guess(guess):
    # main game logic goes here
    flag = False
    global counter
    counter += 1
    try:
        guess = int(guess)
        if secret != None:
            if guess > secret:
                print "Higher"
                print "Guesses remaining:", count - counter
            elif guess < secret:
                print "Lower"
                print "Guesses remaining:", count - counter
            elif guess == secret:
                print "Correct!"
                print "Done in:", counter
                print "Guesses remaining:", count - counter
                new_game()
                flag = True
            else:
                pass
            if counter >= count and flag == False:
                print "You're out of guesses. The correct guess was", secret
                new_game()
        else:
            print "select range first"
            new_game()
    except ValueError:
        print "Invalid input"
        counter -= 1
    inp.set_text('')

# create frame
frame = simplegui.create_frame('Guess the number', 500, 500)

# register event handlers for control elements and start frame
frame.add_button('Range is [0,100)', range100, 100)
frame.add_button('Range is [0,1000)', range1000, 100)
inp = frame.add_input('My label', input_guess, 50)
frame.start()
# call new_game
new_game()


# always remember to check your completed program against the grading rubric
