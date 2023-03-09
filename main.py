
from turtle import *
def circle(c):
    '''
    Function is drawing circle
    TODO: From Anya
    :return:
    '''
    circle(c)
    lt(90)

def semicircle(r):
    '''
    Function is drawing semicircle
    TODO: From Anya
    :return:
    '''
    circle(r,180)
    rt(90)
    bk(r*2)



def square(m):
    '''
    Function is drawing square
    TODO: From Uliana
    :return:
    '''
    for i in range (4):
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

def rectangle(a,b):
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

goto(-300,300)
shape('turtle')
bgcolor('navy')
pd()
square(600)
pu()

goto(-310,300)
color('white','white')
begin_fill()
pd()
rectangle(620,10)
end_fill()
pu()

goto(300,-310)
begin_fill()
pd()
rectangle(10,620)
end_fill()
pu()

goto(-310,-310)
begin_fill()
pd()
rectangle(10,620)
end_fill()
pu()

goto(-300,-310)
begin_fill()
pd()
rectangle(600,10)
end_fill()
pu()

goto(-305,-315)
color('black','black')
begin_fill()
pd()
rectangle(620,5)
end_fill()
pu()

goto(310,-315)
begin_fill()
pd()
rectangle(5,620)
end_fill()
pu()

pu()
done()