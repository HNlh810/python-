import turtle
turtle.penup()
turtle.bk(250)
turtle.pendown()
turtle.pensize(25)
turtle.colormode(255)
turtle.pencolor(139, 0, 255)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 40)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
