import turtle
#turtle.hideturtle()
turtle.speed(0)
filename = turtle.textinput("Load a file","File name:")
myfile = open(filename,"r")
for line in myfile:
    items = line.split("\t")
    x = float(items[1])
    y = float(items[2])
    turtle.goto(x,y)
myfile.close()
turtle.done()
