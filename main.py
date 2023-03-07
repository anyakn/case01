def circle():
    '''
    Function is drawing circle
    :return:
    '''
    circle(n)
    lt(90)

def semicircle():
    '''
    Function id drawing semicircle
    :return:
    '''
    circle(n,180)
    rt(90)


from turtle import*
pu()

goto(-300,300)
shape('turtle')
bgcolor('navy')
pd()
for i in range(4):
    fd(600)
    rt(90)
rt(90)
circle(50,180)


pu()
done()