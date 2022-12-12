import turtle

turtle.speed(0)
turtle.width(10)
turtle.color("green")

turtle.up()
turtle.goto(100,-400)
turtle.left(90)
turtle.down()

turtle.circle(1000,30)
turtle.width(1)
turtle.up()

petal = 0
turtle.color("red")
while petal < 8:
    gap = 10
    circles = 13
    circle_now = 0
    
    turtle.forward(20)
    while circle_now < circles:
        diameter = (circle_now + 1)*1.5*(circles - circle_now)
        turtle.dot(diameter)
        turtle.forward(gap)
        circle_now = circle_now + 1
    turtle.backward(20 + circles * gap)
    turtle.left(360/8)
    petal = petal + 1
turtle.color("yellow")
turtle.dot(100)
turtle.done()
    
    
