import turtle as tr
import numpy as np
tr.shape('turtle')

def krug(n):
    tr.left(90)
    for j in range(n):
        for i in range(180):
            tr.forward(1)
            tr.right(1)
        for i in range(180):
            tr.forward(0.2)
            tr.right(1)

n = int(input())
krug(n)    