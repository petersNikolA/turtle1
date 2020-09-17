import turtle as tr
tr.shape('turtle')
import numpy as np
#tr.tracer(False)
tr.speed(0)
def lico():
    x = 0
    tr.penup()
    tr.goto(100, 0)
    tr.pendown()
    tr.begin_fill()
    tr.color('yellow')
    for i in range(360):
        tr.goto(100 * np.cos(x), 100 * np.sin(x))
        x += 1 * np.pi / 180
    tr.end_fill()
 
def nos():
    tr.goto(0, 0)
    tr.color('black')
    tr.width(10)
    tr.goto(0, 40)

def glasa():
    tr.width(1)
    tr.penup()
    tr.goto(40, 40)
    tr.pendown()
    tr.color('blue')
    tr.begin_fill()
    for i in range(360):
        tr.forward(0.2)
        tr.left(1)
    tr.end_fill()
    tr.penup()
    tr.goto(-40, 40)
    tr.pendown()
    tr.begin_fill()
    for i in range(360):
        tr.forward(0.2)
        tr.left(1)
    tr.end_fill()
    
def rot():
    tr.penup()
    tr.goto(30, -14)
    tr.color('red')
    tr.width(10)
    tr.right(90)
    tr.pendown()
    for i in range(180):
        tr.forward(0.5)
        tr.right(1)
        
        
lico()
nos()
glasa()
rot()
tr.exitonclick()