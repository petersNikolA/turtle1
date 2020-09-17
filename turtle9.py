import turtle as tr
import numpy as np
tr.shape('turtle')

def mnogougol(a, n, r1):
    tr.penup()
    tr.forward(r1)
    tr.pendown()
    k = 3
    for i in range(3, n + 1):
        tr.left(180 - (k - 2) * 180 / (2 * k))
        for j in range(k):
            tr.pendown()
            tr.forward(a)
            tr.left(360 / k)
        tr.right(360 / k)
        a += 20
        tr.penup()
        tr.right((180 - 360 / k) / 2 )
        k += 1
        tr.goto(a / ( 2 * np.sin( np.pi / k)), 0)
    
a = int(input())    
n = int(input())
r1 = a / ( 2 * np.sin( np.pi / 3))
mnogougol(a, n, r1)
tr.exitonclick()