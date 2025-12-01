A,B=map(int,input().split())
r=6.5
diag=(A**2+B**2)**0.5
if diag>2*r:
    print('нет')
else:
    print('да')