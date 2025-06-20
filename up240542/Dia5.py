# Crear lista y mostrarla
frutas = ['banana', 'manzana', 'cereza', 'pera']
print(frutas)

# Añadir elementos
frutas.append('naranja')
frutas.insert(0, 'fresa')
print(frutas)

# Eliminar elementos
frutas.remove('cereza')
ult = frutas.pop()
print(ult, frutas)

# Indexar y contar
print(frutas[1])
print(frutas.index('manzana'))
print(frutas.count('pera'))

# Ordenar y revertir
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

# Copiar y vaciar
copia = frutas.copy()
frutas.clear()
print(frutas, copia)

# Convertir string a lista y viceversa
texto = "Hola PYTHON"
letras = list(texto)
print(letras)
print("".join(letras))

# Loop y comprensión de listas
nums = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in nums]
print(cuadrados)
