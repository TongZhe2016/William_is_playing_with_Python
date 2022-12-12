# Done by TONG, Zhe , 20945220


import turtle
import random
    
### This part of Python code will create the jigsaw pieces when starting up
### by setting up random positions and loading the corresponding image
def createJigsaw():
    global allTurtles
    
    rows = 4
    cols = 4 # Initialize the variables of total number of rows and columns
    
   # Now we go through the jigsaw piece row-column structure
    for row in range(rows):# Go through each row
        for col in range(cols): # Go through each column in this row
            xm = int(turtle.window_width()/2)
            ym = int(turtle.window_height()/2)
            x = random.randint(-xm,xm)
            y = random.randint(-ym,ym)# Generate a random position
            newturtle = turtle.Turtle()# Make a new turtle
            newturtle.up()
            newturtle.speed(0)
            #newturtle.goto(x,y)# Move it to the random position
            newturtle.goto(100*col,-100*row)# Move it to the random position
            file = "image-"+str(row)+"-"+str(col)+".gif"# Build the image file name
            turtle.addshape(file)# Add the image to the turtle system
            newturtle.shape(file)# Apply the new image to this turtle
            newturtle.ondrag(newturtle.goto)# Now fix it so that when this turtle is dragged, it goes to the place where it is dragged
            allTurtles.append(newturtle)# Add the new turtle to the new list of turtles

        
### This part of Python code will only run when the user presses "c" to check the jigsaw
def checkJigsaw():
    turtle.clear()
    checkResult=True # At the start, we assume everything is OK

    for thisTurtle in allTurtles: # Go through every single turtle that we made
        thisX = thisTurtle.xcor() # Get the x coordinate of this turtle
        thisY = thisTurtle.ycor() # Get the y coordinate of this turtle
        
        # An example filename is "image-2-1.gif"
        theFilename = thisTurtle.shape() # Take the image filename of this turtle
        
        lengthOfFilenameWithoutExtension= len(theFilename)-4 # How long the filename is without the ".gif"
        theFilenameWithoutExtension=theFilename[ : lengthOfFilenameWithoutExtension ] # Remove the ".gif"
        FilenameWithoutExtension=theFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

        thisRow=FilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
        thisCol=FilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
        
        thisRow=int(thisRow) # Have to convert the text to an integer before comparing it with a number
        thisCol=int(thisCol) # Have to convert the text to an integer before comparing it with a number

        # We need to check this turtle with all other turtles for position violations
        for compareTurtle in allTurtles: # Go through every other turtle
            compareX = compareTurtle.xcor() # Get the x coordinate of the turtle
            compareY = compareTurtle.ycor() # Get the y coordinate of the turtle
            
            # An example filename is "image-2-1.gif"
            compareFilename = compareTurtle.shape() # Take the image filename of this turtle
            
            lengthOfCompareFilenameWithoutExtension= len(compareFilename)-4 # How long the filename is without the ".gif"
            compareFilenameWithoutExtension=compareFilename[ : lengthOfCompareFilenameWithoutExtension ] # Remove the ".gif"
            FilenameWithoutExtension=compareFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

            compareRow=FilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
            compareCol=FilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
            
            compareRow=int(compareRow) # Have to convert the text to an integer before comparing it with a number
            compareCol=int(compareCol) # Have to convert the text to an integer before comparing it with a number

            # Here, the four position violations will be checked
            # The jigsaw is wrong if any of them fails
            
            # The piece has a smaller column value but is on the right
            if thisCol < compareCol and thisX >= compareX:
                checkResult = False
                break

            # The piece has a larger column value but is on the left
            if thisCol > compareCol and thisX <= compareX:
                checkResult = False
                break
            # The piece has a smaller row value but is on the bottom
            if thisRow < compareRow and thisY <= compareY:
                checkResult = False
                break
            # The piece has a larger row value but is on the top
            if thisRow > compareRow and thisY >= compareY:
                checkResult = False
                break
            
    # Let's check the final result and show an appropriate message
    turtle.up()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.goto(-200,-350)
    if checkResult:
        turtle.write("Congratulations! Your jigsaw is correct!",font=("Arial", 20, "bold"))
    else:
        turtle.write("Oh no! Your jigsaw is WRONG!!",font=("Arial", 20, "bold"))
        turtle.goto(-300,-200)
        turtle.write("Press 'c' again for checking...",font=("Arial", 20,))

### Here is the main part of the program

allTurtles=[] # We will store all the turtles in this list

createJigsaw() # Create the jigsaw pieces
    
turtle.onkeypress(checkJigsaw, "c") # Press 'c' whenever you want to check the jigsaw

turtle.listen() # Listen for key presses

### Note: turtle.mainloop() is exactly the same as turtle.done()
turtle.mainloop() # Keep checking if anything is happening, if so do something appropriate

