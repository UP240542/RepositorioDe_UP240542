edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Falta poco para ser adulto")
else:
    print("Eres menor de edad")

# condicional de una línea
print("Adulto") if edad >= 18 else print("Menor")

# condicional escalonada
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bien")
elif nota >= 50:
    print("Pasaste")
else:
    print("Reprobado")

# operadores lógicos
a = 10
if a > 5 and a < 15:
    print("Entre 5 y 15")
if a == 10 or a == 20:
    print("Es 10 o 20")
