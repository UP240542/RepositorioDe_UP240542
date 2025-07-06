# For loop de 0 a 10
for i in range(11):
    print(i)

# While loop equivalente
i = 0
while i <= 10:
    print(i)
    i += 1

# Bucle inverso
for i in range(10, -1, -1):
    print(i)

# Usar continue y break
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
