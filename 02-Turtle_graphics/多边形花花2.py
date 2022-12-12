import turtle

sidecolor = input("What's the side color?")
insidecolor = input("What's the inside color?")
long = input ("How long?")
thick = input("How thick?")
sides = input("How many sides?")
quantity = input("How many petals?")

long = int(long)
thick = int(thick)
sides = int(sides)
quantity = int(quantity)

angle = 360/quantity
angle2 = 360/sides

turtle.speed(0)
turtle.width(thick)
turtle.color(sidecolor,insidecolor)
i = 0
while i<quantity:
    turtle.begin_fill()
    a=0
    while a<sides:
        turtle.forward(long)
        turtle.left(angle2)
        a = a+1
    turtle.end_fill()
    turtle.left(angle)
    i = i+1
turtle.done()
