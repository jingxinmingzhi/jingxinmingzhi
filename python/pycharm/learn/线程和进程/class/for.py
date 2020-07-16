import turtle
t=turtle.Pen()
t.width(5)
t.color("red")
t.goto(0,80)
t.goto(55,80)
t.penup()
t.goto(0,43)
t.pendown()
t.goto(45,43) #打印“F ”

t.penup()
t.goto(70,43)
t.pendown()
t.goto(70,25)
t.right(90) #画笔向右偏转90度
t.circle(25,180) #画出半圆
t.goto(120,43)
t.penup()
t.goto(180,43)
t.pendown()
t.left(60) #注意要抵消前面的偏转角度
t.circle(25,260) #画出“C”

t.penup()
t.goto(215,80)
t.pendown()
t.goto(215,0)
t.penup()
t.goto(215,30)
t.pendown()
t.goto(255,50)
t.penup()
t.goto(215,30)
t.pendown()
t.goto(270,0) #画出“k”

t.hideturtle()
turtle.done()



