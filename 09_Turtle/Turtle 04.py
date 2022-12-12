import turtle

turtle.speed(0)
def up():
    turtle.goto(turtle.xcor(),turtle.ycor() + 10)
    
def down():
    turtle.goto(turtle.xcor(),turtle.ycor() - 10)
def left():
    turtle.goto(turtle.xcor() - 10,turtle.ycor())
    
def right():
    turtle.goto(turtle.xcor() + 10,turtle.ycor())

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()
turtle.done()
