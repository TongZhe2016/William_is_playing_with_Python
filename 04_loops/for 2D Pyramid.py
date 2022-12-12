import turtle
height = int(input("Height?"))
turtle.speed(0)
turtle.color("brown")
turtle.up()
for i in range(height):
    circles = 0
    turtle.goto(-40*i,-40*i)
    while circles < 2 * i + 1:
        turtle.dot(40)
        turtle.forward(40)
        circles = circles + 1
turtle.done()
