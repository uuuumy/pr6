import turtle as t
x,y=map(int,input('Координаты 1 центра окружности: ').split())
x2,y2=map(int,input('Координаты 2 центра окружности: ').split())
r=int(input('Радиус 1: '))
r2=int(input('Радиус 2: '))
d=((x2-x)**2+(y2-y)**2)**0.5
if d<abs(r-r2):
    print('Одна окружность лежит внутри другой, не касаясь')
elif d==abs(r-r2):
    print('Окружности имеют внутреннее касание')
elif abs(r-r2)<d<r+r2:
    print('Окружности пересекаются')
elif d==r+r2:
    print('Окружности имеют внешнее касание')
else:
    print('Окружности лежат одна вне другой, не касаясь')
t.penup()
t.goto(x,y-r)
t.pendown()
t.circle(r)
t.penup()
t.goto(x2,y2-r2)
t.pendown()
t.circle(r2)
t.hideturtle()
t.done()