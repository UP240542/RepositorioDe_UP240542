# Función pura
def duplica(x): return x * 2

print(list(map(duplica, [1,2,3])))

# Lista por comprensión
cuadrados = [x**2 for x in range(5)]
print(cuadrados)
