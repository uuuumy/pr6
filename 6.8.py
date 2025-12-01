n = int(input('Hомер позиции: '))
if n == 1:
    print(0)
else:
    pos = 1
    for num in range(1, 201):
        if num < 10:        
            pos += 1
            if pos == n:
                print(num)
                break
        elif num < 100:         
            pos += 1
            if pos == n:
                print(num // 10)
                break
            pos += 1
            if pos == n:
                print(num % 10)
                break
        else:                  
            pos += 1
            if pos == n:
                print(num // 100)
                break
            pos += 1
            if pos == n:
                print((num // 10) % 10)
                break
            pos += 1
            if pos == n:
                print(num % 10)
                break
