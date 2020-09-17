import turtle as tr
import numpy as np
tr.shape('turtle')
#tr.tracer(False)
tr.speed(0)

def flower(n):
    x = 0
    for j in range(n // 2):
        for i in range(360):
            tr.forward(1)
            tr.left(1)
        for i in range(360):
            tr.forward(1) 
            tr.right(1)
        tr.left(360 / n)    
            
            
n = int(input())
flower(n)    
tr.exitonclick()