from turtle import *
import functions as fnc

def square_3():
    '''
    Function is drawing bottom left square
    TODO: From Karolina
    :return:
    '''
    goto(0, -200)
    color('darkslateblue', 'darkslateblue')
    begin_fill()
    pd()
    fnc.rectangle(-150, -100)
    end_fill()
    pu()

    goto(-150, -200)
    color('white', 'white')
    begin_fill()
    pd()
    fnc.rectangle(-150, -100)
    end_fill()
    pu()

    color('midnightblue', 'midnightblue')
    begin_fill()
    pd()
    rt(90)
    fnc.semicircle(50, -180)
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
            fnc.circle(10)
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
    fnc.semicircle(50, -180)
    end_fill()
    pu()

    lt(90)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    fnc.rectangle(300, 200)
    end_fill()
    pu()

    goto(-300, 0)
    color('midnightblue', 'midnightblue')
    begin_fill()
    pd()
    fnc.semicircle(150, 180)
    end_fill()
    pu()

    goto(-225, 0)
    color('cornflowerblue', 'cornflowerblue')
    begin_fill()
    pd()
    fnc.semicircle(75, 180)
    end_fill()
    pu()
