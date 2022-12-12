class square:
    def __init__(self, x, y, length, color):
        self.length = length
        self.x = x
        self.y = y
        self.color = color
    def area(self):
        return self.length * self.length
    def draw(self):
        import turtle
        turtle.tracer(False)
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.color(self.color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.length)
            turtle.left(90)
        turtle.end_fill()

class chessboard:
    def __init__(self,l,a,b,color1,color2):
        self.l = l
        self.a = a
        self.b = b
        self.color1 = color1
        self.color2 = color2
    def draw(self):
        for col in range(self.a):
            for row in range(self.b):
                if (col+row)%2:
                    asquare = square(self.l*col,self.l*row,self.l,self.color1)
                    asquare.draw()
                else:
                    bsquare = square(self.l*col,self.l*row,self.l,self.color2)
                    bsquare.draw()
    def print(self):
        print('haha')
mysquare = square(20,10,200,'red')
mychessboard = chessboard(10,20,20,'black','blue')

print(mysquare.area())
mysquare.length = 100
print(mysquare.area())
mysquare.draw()
mychessboard.draw()
mychessboard.print()
