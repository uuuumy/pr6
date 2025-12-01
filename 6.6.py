N=int(input('Кол-во малышей: '))
K=int(input('Кол-во мест: '))
M=int(input('Кол-во минут: '))
print(((N//K)*M*2)+((N-K*(N//K))*M*2))
