import turtle as tr
tr.shape('turtle')
import numpy as np
#tr.tracer(False)
tr.speed(0)

def zvezda(n, l):
    for i in range(n):
        tr.forward(l)
        tr.right(180 - 180 / n)


l = int(input())
n = int(input())
zvezda(n, l)
tr.exitonclick()