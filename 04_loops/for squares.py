import turtle
turtle.speed(0)
turtle.pencolor("yellow")
turtle.fillcolor("red")
for i in range(20,0,-1):
    l = 10 * i
    side = 0
    turtle.begin_fill()
    while side < 4:
        turtle.forward(l)
        turtle.left(90)
        side = side + 1
    turtle.end_fill()
turtle.done()
