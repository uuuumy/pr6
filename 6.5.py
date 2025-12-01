x=input().split("-")
x1=x[0]
x2=x[1]
x1_1=x1[0]
x1_2=int(x1[1])
x2_1=x2[0]
x2_2=int(x2[1])
x1_1=int(x1_1.replace("a",'1').replace('b','2').replace('c','3')\
         .replace('d','4').replace('e','5').replace('f','6')\
         .replace('g','7').replace('h','8'))
x2_1=int(x2_1.replace("a",'1').replace('b','2').replace('c','3')\
         .replace('d','4').replace('e','5').replace('f','6')\
         .replace('g','7').replace('h','8'))
if abs(x1_1-x2_1)*abs(x1_2-x2_2)==2:
    print('верно')
else:
    print('ошибка')