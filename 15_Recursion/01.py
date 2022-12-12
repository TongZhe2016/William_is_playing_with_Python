import turtle

turtle.tracer(False)
turtle.setworldcoordinates(0,0,255,255)
turtle.up()
turtle.hideturtle()
turtle.bgcolor('black')

m = 4

done = 0
def hole(x,y,size):
    global done
    if done < m:
        turtle.goto(x-size/2,y-size/2)
        turtle.color('white')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()

def carpet(x,y,size,done):
    hole(x,y,size)
    if done < m:
        carpet(x+3*size/4,y+3*size/4,size/8,done+1)
        carpet(x+3*size/4,y-3*size/4,size/8,done+1)
        carpet(x-3*size/4,y+3*size/4,size/8,done+1)
        carpet(x-3*size/4,y-3*size/4,size/8,done+1)
    
carpet(127,127,127,0)
