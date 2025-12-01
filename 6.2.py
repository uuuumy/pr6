A,B=map(int,input('Параметры отверстия: ').split())
C,D,E=map(int,input('Параметры кирпича(высота,длина,ширина): ').split())
onediag=(C**2+E**2)**0.5
twodiag=(C**2+D**2)**0.5
glgiag=(A**2+B**2)**0.5
if onediag<glgiag or twodiag<glgiag:
    print('да')
else:
    print('нет')