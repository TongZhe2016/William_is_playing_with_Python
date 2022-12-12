import turtle

turtle.speed(0)

def jump(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

turtle.ondrag(turtle.goto)

turtle.onscreenclick(jump)

turtle.done()
