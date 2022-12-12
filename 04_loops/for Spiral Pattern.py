import turtle
turtle.speed(0)
turtle.color("purple")
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(0,400,1):
    turtle.forward(i)
    turtle.right(89)
for i in range(401,0,-1):
    turtle.forward(i)
    turtle.right(89)
turtle.end_fill()
turtle.done()
