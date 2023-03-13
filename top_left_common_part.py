from turtle import *

import functions as fnc
def square_1():
    '''
    Function is drawing top left square
    TODO: From Anya, Karolina and Uliana
    :return:
    '''
    goto(-300, 300)
    color('midnightblue', 'midnightblue')
    begin_fill()
    pd()
    fnc.square(300)
    end_fill()
    pu()

    goto(-150, 0)
    color('darkslateblue', 'darkslateblue')
    begin_fill()
    pd()
    fnc.circle1(150)
    end_fill()
    pu()

    goto(0, 0)
    color('white', 'white')
    begin_fill()
    pd()
    lt(45)
    fnc.triangle(300 * (2 ** 0.5))
    end_fill()
    pu()
    rt(45)

    goto(-150, 150)
    color('darkslateblue', 'darkslateblue')
    rt(135)
    begin_fill()
    pd()
    fnc.triangle(150 * 2 ** 0.5)
    end_fill()
    pu()
    lt(135)

    goto(-300, 300)
    rt(135)
    color('darkslateblue', 'darkslateblue')
    begin_fill()
    pd()
    fnc.triangle(150 * 2 ** 0.5)
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
        fnc.rectangle(3, 150)
        end_fill()
        pu()
        y += 15

    goto(-225, 0)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    rt(90)
    fnc.semicircle(75, -180)
    end_fill()
    pu()
