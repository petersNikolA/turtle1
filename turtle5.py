def sqares(n):
    turtle.shape('turtle')
    x = 10
    while n > 0:
        turtle.pendown()
        count = 4
        while count > 0:
            turtle.forward(x)
            turtle.left(90)
            count -= 1
        turtle.penup()
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.backward(10)
        x += 20
        n -= 1
import turtle
n = int(input())
sqares(n)