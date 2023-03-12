
from turtle import *


def circle1(c):
    '''
    Function is drawing circle
    TODO: From Anya
    :return:
    '''
    circle(c)
    lt(90)


def semicircle(r, ang):
    '''
    Function is drawing semicircle
    TODO: From Anya
    :return:
    '''
    rt(90)
    circle(r, ang)
    rt(90)
    bk(r*2)


def square(m):
    '''
    Function is drawing square
    TODO: From Uliana
    :return:
    '''
    for i in range(4):
        fd(m)
        rt(90)


def triangle(n):
    '''
    Function is drawing triangle
    TODO: From Uliana
    :return:
    '''
    fd(n)
    lt(135)
    fd(2**0.5*n/2)
    lt(90)
    fd(2**0.5*n/2)
    lt(135)


def rectangle(a, b):
    '''
    Function is drawing rectangle
    TODO: From Karolina
    :return:
    '''
    for _ in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)


pu()
speed(-1)


goto(-300, 300)
shape('turtle')
bgcolor('navy')
pd()
square(600)
pu()

goto(-310, 300)
color('white', 'white')
begin_fill()
pd()
rectangle(620, 10)
end_fill()
pu()

goto(300, -310)
begin_fill()
pd()
rectangle(10, 620)
end_fill()
pu()

goto(-310, -310)
begin_fill()
pd()
rectangle(10, 620)
end_fill()
pu()

goto(-300, -310)
begin_fill()
pd()
rectangle(600, 10)
end_fill()
pu()

goto(-305, -315)
color('black', 'black')
begin_fill()
pd()
rectangle(620, 5)
end_fill()
pu()

goto(310, -315)
begin_fill()
pd()
rectangle(5, 620)
end_fill()
pu()

goto(0, 0)
color('midnightblue', 'midnightblue')
begin_fill()
pd()
square(300)
end_fill()
pu()

goto(0, -150)
lt(45)
color('white', 'white')
begin_fill()
pd()
triangle(150*(2**0.5))
end_fill()
pu()
rt(45)

goto(0, -300)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
semicircle(150, -180)
end_fill()
pu()

goto(50, -300)
color('white', 'white')
begin_fill()
pd()
semicircle(100, -180)
end_fill()
pu()


goto(100, -300)
color('darkslateblue', 'darkslateblue')
begin_fill()
pd()
semicircle(50, -180)
end_fill()
pu()


x = 150
y = 0
for i in range(4):
    goto(x, y)
    for j in range(4):
        color('white', 'white')
        rt(45)
        begin_fill()
        pd()
        triangle(30 * (2 ** 0.5))
        end_fill()
        lt(45)
        pu()
        x += 40
        goto(x, y)
    x = 150
    y -= 40

goto(0, -200)
color('darkslateblue', 'darkslateblue')
begin_fill()
pd()
rectangle(-150, -100)
end_fill()
pu()

goto(-150, -200)
color('white', 'white')
begin_fill()
pd()
rectangle(-150, -100)
end_fill()
pu()

color('midnightblue', 'midnightblue')
begin_fill()
pd()
rt(90)
semicircle(50, -180)
end_fill()
pu()

x = -170
y = -230
for _ in range(3):
    goto(x, y)
    for _ in range(3):
        color('darkslateblue', 'darkslateblue')
        begin_fill()
        pd()
        circle(10)
        end_fill()
        pu()
        x += - 25
        goto(x, y)
    x += 75
    y -= 25

goto(-300, -200)
color('midnightblue', 'midnightblue')
begin_fill()
pd()
semicircle(50, -180)
end_fill()
pu()

lt(90)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
rectangle(300, 200)
end_fill()
pu()

goto(-300, 0)
color('midnightblue', 'midnightblue')
begin_fill()
pd()
semicircle(150, 180)
end_fill()
pu()

goto(-225, 0)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
semicircle(75, 180)
end_fill()
pu()


goto(0, 150)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
rectangle(300, 150)
end_fill()
pu()

goto(0, 0)
color('white', 'white')
begin_fill()
pd()
rectangle(300, 150)
end_fill()
pu()

goto(0, 0)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
triangle(150)
end_fill()
pu()

goto(75, 150)
color('white', 'white')
begin_fill()
pd()
semicircle(75, -180)
end_fill()
pu()

goto(75, 150)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
triangle(150)
end_fill()
pu()

lt(180)
goto(225, 150)
color('midnightblue', 'midnightblue')
begin_fill()
pd()
triangle(150)
end_fill()
rt(180)
pu()

rt(135)
goto(300, 150)
color('darkslateblue', 'darkslateblue')
begin_fill()
pd()
triangle(212)
end_fill()
pu()
lt(135)

goto(75, 300)
color('darkslateblue', 'darkslateblue')
begin_fill()
pd()
semicircle(75, 180)
end_fill()
pu()

goto(-300, 300)
color('midnightblue', 'midnightblue')
begin_fill()
pd()
square(300)
end_fill()
pu()

goto(-150, 0)
color('darkslateblue', 'darkslateblue')
begin_fill()
pd()
circle1(150)
end_fill()
pu()

goto(0, 0)
color('white', 'white')
begin_fill()
pd()
lt(45)
triangle(300*(2**0.5))
end_fill()
pu()
rt(45)

goto(-150, 150)
color('darkslateblue', 'darkslateblue')
rt(135)
begin_fill()
pd()
triangle(150*2**0.5)
end_fill()
pu()
lt(135)

goto(-300, 300)
rt(135)
color('darkslateblue', 'darkslateblue')
begin_fill()
pd()
triangle(150*2**0.5)
end_fill()
lt(135)
pu()

x = -75
y = 140
for _ in range(3):
    goto(x, y)
    color('black', 'black')
    begin_fill()
    pd()
    rectangle(3, 150)
    end_fill()
    pu()
    y += 15

goto(-225, 0)
color('cornflowerblue', 'cornflowerblue')
begin_fill()
pd()
rt(90)
semicircle(75, -180)
end_fill()
pu()

pu()
done()
