from turtle import *
import functions as fnc

def square_2():
    '''
    Function is drawing top right square
    TODO: From Uliana
    :return:
    '''
    goto(0, 150)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    fnc.rectangle(300, 150)
    end_fill()
    pu()

    goto(0, 0)
    color('white', 'white')
    begin_fill()
    pd()
    fnc.rectangle(300, 150)
    end_fill()
    pu()

    goto(0, 0)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    fnc.triangle(150)
    end_fill()
    pu()

    goto(75, 150)
    color('white', 'white')
    begin_fill()
    pd()
    fnc.semicircle(75, -180)
    end_fill()
    pu()

    goto(75, 150)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    fnc.triangle(150)
    end_fill()
    pu()

    lt(180)
    goto(225, 150)
    color('midnightblue', 'midnightblue')
    begin_fill()
    pd()
    fnc.triangle(150)
    end_fill()
    rt(180)
    pu()

    rt(135)
    goto(300, 150)
    color('darkslateblue', 'darkslateblue')
    begin_fill()
    pd()
    fnc.triangle(212)
    end_fill()
    pu()
    lt(135)

    goto(75, 300)
    color('darkslateblue', 'darkslateblue')
    begin_fill()
    pd()
    fnc.semicircle(75, 180)
    end_fill()
    pu()

