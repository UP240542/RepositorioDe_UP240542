try:
    x = 1 / 0
except ZeroDivisionError:
    print("División por cero")
else:
    print("Todo bien")
finally:
    print("Esto siempre se ejecuta")
