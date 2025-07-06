import datetime

hoy = datetime.date.today()
ahora = datetime.datetime.now()
print(hoy, ahora)
# Formatos personalizados
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))
