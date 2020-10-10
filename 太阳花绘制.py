import turtle
turtle.penup()
turtle.bk(100)
turtle.pendown()
turtle.color("red","yellow")
turtle.begin_fill()
for  _ in range(37):
    turtle.fd(200)
    turtle.left(170)
turtle.end_fill()
turtle.mainloop()