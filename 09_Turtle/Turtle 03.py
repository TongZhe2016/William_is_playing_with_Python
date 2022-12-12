import turtle
def func(x,y):
    turtle.goto(x,y)

turtle.speed(1)
turtle.shape('circle')
turtle.pensize(3)
turtle.ondrag(turtle.goto)
turtle.done()
