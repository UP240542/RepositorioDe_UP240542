def shout(func):
    def wrapper(msg):
        return func(msg).upper()
    return wrapper

@shout
def saludo(msg):
    return msg

print(saludo("hola"))
