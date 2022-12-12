import turtle

turtle.tracer(False)
turtle.setworldcoordinates(0,0,255,255)
turtle.up()
turtle.hideturtle()
turtle.bgcolor('black')

max_depth = 8

def triangle(x,y,size,color):
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def carpet(x,y,size,depth):
    if not depth % 2:
        color = 'white'
    if depth % 2:
        color = 'black'
    triangle(x,y,size,color)
    if depth < max_depth:
        carpet(x,y,size/2,depth+1)
        carpet(x+size/2,y,size/2,depth+1)
        carpet(x+size/4,y+size*0.43301270189,size/2,depth+1)

carpet(0,0,255,0)

turtle.done()
