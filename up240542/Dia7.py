frutas = {'manzana', 'banana', 'cereza'}
print(frutas, len(frutas))

frutas.add('pera')
frutas.update(['kiwi', 'mango'])
print(frutas)

frutas.remove('banana')  # error si no existe
frutas.discard('papaya')  # no lanza error
print(frutas.pop())  # quita uno al azar
print('pera' in frutas)

# operaciones con sets
A = {1,2,3}
B = {3,4,5}
print(A.union(B), A.intersection(B), A.difference(B), A.symmetric_difference(B))

# borrar set
frutas.clear()
del frutas
