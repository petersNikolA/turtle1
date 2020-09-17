import turtle as tr
import numpy as np
tr.shape('turtle')
tr.tracer(False)
#tr.speed(0)

def babochka(n):
    x = 0
    for j in range(n // 2):
        for i in range(360):
            tr.forward(0.5 + x)
            tr.left(1)
        for i in range(360):
            tr.forward(0.5 + x) 
            tr.right(1)
        x += 0.1
            
            
n = int(input())
babochka(n)    
tr.exitonclick()