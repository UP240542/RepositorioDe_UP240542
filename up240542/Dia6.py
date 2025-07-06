mi_tupla = ('manzana', 'banana', 'cereza', 'pera', 'kiwi')
print(mi_tupla)
print(len(mi_tupla))  # longitud
print(mi_tupla[0], mi_tupla[-1])
print(mi_tupla[1:4])  # slicing

# convertir a lista y modificar
lista = list(mi_tupla)
lista.append('mango')
mi_tupla = tuple(lista)
print(mi_tupla)

# check
print('kiwi' in mi_tupla)
# borrar la tupla
del mi_tupla
