k=int(input())
flag=0
for i in range(k // 7 + 1):
    r=k-7*i
    if r>=0 and r%5==0:
        flag=1
if flag==1:
    print('да')
else:
    print('нет')