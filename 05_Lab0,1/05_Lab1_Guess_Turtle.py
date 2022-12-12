'''
Made By: TONG, Zhe
SID: 20945220
'''

import random               # Import the 'random' library
import turtle               # Import the 'turtle' library

target = 0                  # We will store the number to be guessed here
finished = False            # This is true if the game has finished
guess_input_text = ""       # We will store text in here
guess_input = 0             # We will store a number in here

target = random.randint(1,100)
                            # Generate a new integer random number

number_attempted = 0
y = 300
turtle.up()
turtle.speed(0)
turtle.goto(-350,y)
turtle.write("I'm thinking of a number, What is it?",font=("Arial", 20, "bold"))
y = y - 20
turtle.goto(-350,y)
# Do the main game loop
while not finished:
    guess_input_text = turtle.textinput("Guessing Gmae","Please enter a number between 1 and 100:")
    guess_input = int(guess_input_text)
                            # Get the user's guess
    if guess_input < 1 or guess_input > 100:
        turtle.write("Wrong range.",font=("Arial", 20, "bold"))
    elif guess_input > target:
        turtle.write("Too High.",font=("Arial", 20, "bold"))
    elif guess_input < target:
        turtle.write("Too Low.",font=("Arial", 20, "bold"))
    else:
        finished = True
    number_attempted = number_attempted + 1
    y = y - 20
    turtle.goto(-350,y)
                            # Check the user's guess
    
turtle.write("you got it! My number is " + str(target),font=("Arial", 20, "bold"))
y = y - 20
turtle.goto(-350,y)
turtle.write("It took you " + str(number_attempted) + " guesses to get the number!",font=("Arial", 20, "bold"))
turtle.done()               # At this point, the game is finished
