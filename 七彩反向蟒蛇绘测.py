import turtle
turtle.setup(1100,350)
turtle.penup()
turtle.fd(400)
turtle.pendown()
turtle.pensize(25)
turtle.colormode(255)
turtle.pencolor(255,0,0)
turtle.seth(220)
for i in range(7):
    if i == 1:
        turtle.pencolor(255,165,0)
    if i == 2:
        turtle.pencolor(255,255,0)
    if i == 3:
        turtle.pencolor(0,128,0)
    if i == 4:
        turtle.pencolor(0,255,255)
    if i == 5:
        turtle.pencolor(0,0,255)
    if i == 6:
        turtle.pencolor(139,0,255)
    turtle.circle(-40,80)
    turtle.circle(40,80)
turtle.circle(-40,40)
turtle.fd(40)
turtle.circle(-16,180)
turtle.fd(40 * 2/3)
turtle.done()
