import turtle as t
x,y=map(int,input('Координаты 1 левой верхней точки: ').split())
x2,y2=map(int,input('Координаты 1 правой нижней точки: ').split())
x3,y3=map(int,input('Координаты 2 левой верхней точки: ').split())
x4,y4=map(int,input('Координаты 2 правой нижней точки: ').split())
def f(x,y,z,h):
    x_min=min(x, z)
    x_max=max(x, z)
    y_min=min(h, y)
    y_max=max(h, y)
    return x_min, y_min, x_max, y_max
x1_min, y1_min, x1_max, y1_max = f(x, y, x2, y2)
x2_min, y2_min, x2_max, y2_max = f(x3, y3, x4, y4)
if (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max):
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif (x1_min < x2_max and x1_max > x2_min and y1_min < y2_max and y1_max > y2_min):
    if (x1_min > x2_min and x1_max < x2_max and y1_min > y2_min and y1_max < y2_max) or \
       (x2_min > x1_min and x2_max < x1_max and y2_min > y1_min and y2_max < y1_max):
        print("Один прямоугольник лежит внутри другого, не касаясь")
    else:
        print("Прямоугольники пересекаются")
else:
    print("Прямоугольники имеют касание")

t.penup()
t.goto(x,y)
t.pendown()
t.goto(x2,y)
t.goto(x2,y2)
t.goto(x,y2)
t.goto(x,y)
t.penup()
t.goto(x3,y3)
t.pendown()
t.goto(x4,y3)
t.goto(x4,y4)
t.goto(x3,y4)
t.goto(x3,y3)
t.hideturtle()
t.done()
