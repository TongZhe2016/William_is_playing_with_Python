import turtle

r = int(input("r?"))

x1 = int(input("x?"))
y1 = int(input("y?"))

turtle.up()
turtle.speed(0)
turtle.color("green")

x = 0
while x<x1:
    y = 0
    while y<y1:
        turtle.goto(r*x,r*y)
        turtle.dot(r)
        y = y + 1
    x = x + 1


turtle.done()
