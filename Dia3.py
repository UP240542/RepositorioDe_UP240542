# Día 3 - Operadores con entrada del usuario

# Solicitar valores al usuario
a = int(input("Ingresa el primer número (a): "))
b = int(input("Ingresa el segundo número (b): "))

# Realizar operaciones
print(f"\nSuma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División (flotante): {a} / {b} = {a / b if b != 0 else 'Indefinido (división entre 0)'}")
print(f"División entera: {a} // {b} = {a // b if b != 0 else 'Indefinido'}")
print(f"Módulo: {a} % {b} = {a % b if b != 0 else 'Indefinido'}")
print(f"Exponenciación: {a} ** {b} = {a ** b}")
