from turtle import *

ht()

setup(400,800,0,0)
seth(0)

pensize(3)

pencolor("black")

pu()  #penup()

goto(0,100)

pd()  #pendown()
fillcolor("brown")

begin_fill()

circle(100)

end_fill()
pu()

goto(0,150)

pd()

fillcolor("white")

begin_fill()

pencolor("white")

circle(30)

end_fill()

pencolor("black")

pu()

goto(0,179)

lt(45)

fd(35)

rt(45)

pd()

fillcolor("black")

begin_fill()

circle(10)

end_fill()
pu()

goto(0,179)

lt(135)

fd(35)

rt(135)

pd()

fillcolor("black")

begin_fill()

circle(10)

end_fill()
pu()

goto(0,180)

pd()

fillcolor("black")

begin_fill()

circle(6)

end_fill()
goto(-3,180)

seth(-135)

pensize(5)

fd(12)
pu()

goto(3,180)

pd()

seth(-45)

pensize(5)

fd(12)
pensize(3)

pu()

goto(0,200)

seth(30)

fd(100)

pd()

fillcolor("brown")

begin_fill()

circle(30,215)

end_fill()

pu()

goto(0,200)

seth(150)

fd(100)

pd()

fillcolor("brown")

begin_fill()

circle(-30,215)

end_fill()

pu()

goto(50*pow(3,0.5),152) #pow(x,y)=x**y

seth(60)

pd()

fillcolor("brown")

begin_fill()

circle(-15,180)

circle(-130,30)

seth(-90)

circle(-1000,8)
for i in range(2):
    seth(-90)

    circle(-27,180)

lt(10)

circle(-1000,8)

seth(150)

circle(-130,30)

circle(-16,180)

circle(100,120)

end_fill()
pu()

goto(0,80)

seth(0)

pd()

pencolor("black")

fillcolor("black")

begin_fill()

circle(-40)

end_fill()

done()


