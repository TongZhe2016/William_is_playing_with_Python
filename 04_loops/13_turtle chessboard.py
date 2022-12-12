import turtle

turtle.up()
turtle.color("gray")
turtle.speed(0)
row = int(turtle.textinput("row","input"))
col = int(turtle.textinput("col","input"))
l = int(turtle.textinput("l","input"))

for a in range(row):
    turtle.goto(0,l*a)
    for b in range(col):
        if (a + b) % 2:
            turtle.forward(l)
            continue
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(l)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(l)
turtle.goto(0,0)
turtle.down()
turtle.forward(l*(b+1))
turtle.left(90)
turtle.forward(l*(a+1))
turtle.left(90)
turtle.forward(l*(b+1))
turtle.left(90)
turtle.forward(l*(a+1))
turtle.left(90)
turtle.done()
