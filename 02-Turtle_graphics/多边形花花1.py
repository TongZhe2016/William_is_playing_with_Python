import turtle
size = input ("How long?")
k = input("How thick?")
b = input("How many sides?")
size = int(size)
k = int(k)
b = int(b)
angle = 360/b
turtle.speed(0)
turtle.width(k)
turtle.color("yellow","red")
#turtle.up()
#turtle.goto(-size/2,-3**0.5*size/2)
#turtle.down()
i = 1
c = 360/(180-angle)
while i<=c:
    turtle.begin_fill()
    a=0
    while a<b:
        turtle.forward(size)
        turtle.left(angle)
        a = a+1
    turtle.end_fill()
    turtle.left(180-angle)
    i = i+1
turtle.done()
