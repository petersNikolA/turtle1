import turtle
turtle.shape('turtle')

def pavuk(n):
    for i in range(n):
        turtle.right(360 / n)
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)

n = int(input())
pavuk(n)