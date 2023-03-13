from turtle import *

import functions as fnc

def square_4:
    '''
    Function is drawing bottom right square
    TODO: From Anya
    :return:
    '''
    goto(-300, 300)
    shape('turtle')
    bgcolor('navy')
    pd()
    fnc.square(600)
    pu()

    goto(-310, 300)
    color('white', 'white')
    begin_fill()
    pd()
    fnc.rectangle(620, 10)
    end_fill()
    pu()

    goto(300, -310)
    begin_fill()
    pd()
    fnc.rectangle(10, 620)
    end_fill()
    pu()

    goto(-310, -310)
    begin_fill()
    pd()
    fnc.rectangle(10, 620)
    end_fill()
    pu()

    goto(-300, -310)
    begin_fill()
    pd()
    fnc.rectangle(600, 10)
    end_fill()
    pu()

    goto(-305, -315)
    color('black', 'black')
    begin_fill()
    pd()
    fnc.rectangle(620, 5)
    end_fill()
    pu()

    goto(310, -315)
    begin_fill()
    pd()
    fnc.rectangle(5, 620)
    end_fill()
    pu()

    goto(0, 0)
    color('midnightblue', 'midnightblue')
    begin_fill()
    pd()
    fnc.square(300)
    end_fill()
    pu()

    goto(0, -150)
    lt(45)
    color('white', 'white')
    begin_fill()
    pd()
    fnc.triangle(150 * (2 ** 0.5))
    end_fill()
    pu()
    rt(45)

    goto(0, -300)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    fnc.semicircle(150, -180)
    end_fill()
    pu()

    goto(50, -300)
    color('white', 'white')
    begin_fill()
    pd()
    fnc.semicircle(100, -180)
    end_fill()
    pu()

    goto(100, -300)
    color('darkslateblue', 'darkslateblue')
    begin_fill()
    pd()
    fnc.semicircle(50, -180)
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
            fnc.triangle(30 * (2 ** 0.5))
            end_fill()
            lt(45)
            pu()
            x += 40
            goto(x, y)
        x = 150
        y -= 40



