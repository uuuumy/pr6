n,m=map(int,input().split())
k=int(input())
if k< n*m and (k%n==0 or k%m==0):
    print('успешно')
else:

    print('неосуществимо')
