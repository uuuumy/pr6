x=input('Клетка: ')
a=x[0]
b=x[1]
if (a in 'aceg') and int(b)%2==0:
    print('белый')
else:
    if (a in 'aceg') and int(b)%2!=0:
        print('черный')
if (a in 'bdfh') and int(b)%2==0:
    print('черный')
else:
    if (a in 'bdfh') and int(b)%2!=0:
        print('белый')
