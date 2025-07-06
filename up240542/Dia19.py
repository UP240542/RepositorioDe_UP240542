# Leer
with open('data.txt', 'r') as f:
    data = f.read()

# Escribir (sobrescribe o crea)
with open('output.txt', 'w') as f:
    f.write("Hola mundo")

# Agregar
with open('log.txt', 'a') as f:
    f.write("Otro registro\n")
