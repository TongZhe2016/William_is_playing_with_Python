import turtle
turtle.speed(0)
def a(x,y):
    global myfile
    turtle.ondrag(None)
    turtle.goto(x,y)
    this = 'drag'+'\t'+str(x)+'\t'+str(y)+"\n"
    myfile.write(this)
    turtle.ondrag(a)
filename = turtle.textinput("Save positions","Filename:")
myfile = open(filename, "wt")
turtle.ondrag(a)
turtle.listen()
turtle.mainloop()
myfile.close()
