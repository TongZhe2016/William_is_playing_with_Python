# Fireworks in Hong Kong
import random
import turtle
import time
import playsound

# Initialize the turtle module:
turtle.up()
turtle.setup(900,564)
turtle.bgpic("hong_kong.gif")
turtle.shape("circle")
turtle.color("red")
turtle.hideturtle()
turtle.speed(0)

# Initialize variables used in the program
f_r_m = int(turtle.textinput("Firworks in Hong Kong","Please input the biggest size of the fireworks:"))
f_q = int(turtle.textinput("Firworks in Hong Kong","Please enter the number of fireworks you would like:"))
firework_colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]

# Every firework per for loop:
for i in range(f_q):
    
    # Clear the sky (screen) for every five fireworks:
    if i > 0 and i % 5 == 0:
        time.sleep(0.5)
        turtle.clear()
        
    # Determine the starting point:
    sx = random.randint(-450,450)
    sy = random.randint(-282,0)
    
    # Determine the ending point:
    ex = random.randint(-450,450)
    ey = random.randint(0,282)
    
    # Shoot a firework from the start to the destination:
    turtle.speed(5)
    turtle.color("red")
    turtle.goto(sx,sy)
    turtle.showturtle()
    turtle.goto(ex,ey)
    turtle.hideturtle()
    turtle.speed(0)

    ## Firework exploding:
    size = random.randint(10,f_r_m)                       # Set the size of the firework
    lines = random.randint(8,15)                        # Set the number of lines of the firework
    turtle.color(firework_colors[random.randint(0,6)])  # Set the color of the firework
    playsound.play("explosion.wav")
    
    # Every ring per for loop:
    for r in range(int(size/10)):
        turtle.forward(10*r)
        turtle.setheading(90)
        turtle.tracer(False)
        # Every dot per for loop
        for _ in range(lines):
            turtle.dot(r)
            turtle.circle(10*r,360/lines)
            
        ey = ey - 5                                 # Up a little bit to make gravity looks exists
        turtle.goto(ex,ey)
        turtle.setheading(0)
        turtle.tracer(True)
    
turtle.done()