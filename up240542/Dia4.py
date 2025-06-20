# Declarar un string, mostrarlo y su longitud
mensaje = "¡Hola, mundo!"
print(mensaje)
print(len(mensaje))

# Convertir a mayúsculas y minúsculas
print(mensaje.upper())
print(mensaje.lower())

# Extraer subcadenas
sub = mensaje[2:7]
print(sub)

# Dividir por espacios y unir con otro separador
palabras = mensaje.split()
print(palabras)
print(" - ".join(palabras))

# Reemplazar palabra
nuevo = mensaje.replace("Hola", "Hello")
print(nuevo)

# Buscar posición de 'mundo'
pos = mensaje.find("mundo")
print(pos)  # si no lo encuentra, devuelve -1

# Comprobar si empieza/termina con
print(mensaje.startswith("¡"))
print(mensaje.endswith("!"))

# Recorrer cada carácter
for c in mensaje:
    print(c)
