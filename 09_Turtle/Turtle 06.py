import turtle
turtle.setworldcoordinates(-100,-100,1000,1000)
turtle.hideturtle()
turtle.speed(0)

datas = []

def drawrectangle(a,b):
    for _ in range(2):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)

def drawcoordinate(x,y):
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.goto(1000,0)
    turtle.dot(10)
    turtle.goto(0,0)
    turtle.goto(0,1000)
    turtle.dot(10)
    turtle.goto(0,0)
    for a in range(int(x)+1):
        turtle.goto(a*1000/x,0)
        turtle.dot(5)
        turtle.write(str(a))
        turtle.goto(0,0)
    for b in range(int(y)+2):
        turtle.goto(0,b*1000/(y+1))
        turtle.dot(5)
        turtle.write(str(b))
        turtle.goto(0,0)
    turtle.down()

quantity = int(turtle.textinput("Bar Chart Maker","How many data?(0-1000)"))
a = 1000/quantity

for i in range(quantity):
    number = int(turtle.textinput("Bar Chart Maker","What's the "+str(i)+" data?"))
    datas.append(number)

maxvalue = max(datas)
drawcoordinate(quantity,maxvalue)

for number in datas:
    drawrectangle(a,number*1000/(maxvalue+1))
    turtle.forward(a)

