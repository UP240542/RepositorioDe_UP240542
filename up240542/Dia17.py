try:
    val = int(input("Dame un número:"))
except ValueError:
    print("No es un número")
else:
    print("Buen número:", val)
finally:
    print("Esto siempre se ejecuta")
