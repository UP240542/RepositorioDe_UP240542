def cuenta_atras(n):
    while n > 0:
        yield n
        n -= 1

for i in cuenta_atras(5):
    print(i)
