from turtle import *
import bottom_right_anyas_part as br
import bottom_left_karolinas_part as bl
import top_left_common_part as tl

pu()
speed(-1)

br.square_4()
bl.square_3()
tl.square_1()

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

pu()
done()

