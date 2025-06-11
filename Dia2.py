# 1. Números y operaciones
a = 5
b = 4

print("Suma:", a + b)           # 9
print("Resta:", a - b)          # 1
print("Multiplicación:", a * b) # 20
print("División:", a / b)       # 1.25
print("Módulo:", a % b)         # 1
print("Exponente:", a ** b)     # 625
print("División entera:", a // b) # 1

# 2. Área de un triángulo
base = 10
altura = 5
area_triangulo = 0.5 * base * altura
print("Área del triángulo:", area_triangulo)

# 3. Obtener entrada del usuario (comentado para no bloquear el script)
# base = float(input("Base: "))
# altura = float(input("Altura: "))
# print("Área:", 0.5 * base * altura)

# 4. Variables personales
nombre = "Orlando"
apellido = "Vargas"
pais = "México"
edad = 22

print(f"Me llamo {nombre} {apellido}, tengo {edad} años y soy de {pais}.")

# 5. Compara longitudes
print("¿Nombre y apellido tienen la misma longitud?", len(nombre) == len(apellido))

# 6. Compara números
num1 = 10
num2 = 20
print("num1 > num2?", num1 > num2)

# 7. Compara cadenas
print("apple" > "banana")  # False

# 8. Conversión de tipos
num_str = "10"
num_int = int(num_str)
print("Conversión:", num_int + 5)  # 15

# 9. Cálculo de círculo
radio = 5
pi = 3.14159
area_circulo = pi * radio ** 2
circunferencia = 2 * pi * radio
print("Área:", area_circulo)
print("Circunferencia:", circunferencia)
