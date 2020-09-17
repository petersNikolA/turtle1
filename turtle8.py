import turtle
turtle.shape('turtle')

def sqspiral(n):
    l = 5
    while n > 0:
        l += 5
        for i in range(2):
            turtle.forward(l)
            turtle.left(90)
        n -= 1      

n = int(input())
sqspiral(n)        