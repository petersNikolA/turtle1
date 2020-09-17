import turtle as tr
import numpy as np
tr.shape('turtle')

def spiral():
    x = 0
    r = 5.0
    tr.penup()
    tr.goto(r, 0)
    tr.pendown()
    while True:
        tr.goto(r * np.cos(x), r * np.sin(x))
        x += 1 * np.pi / 180
        r += 0.05
    
spiral()