import re

texto = "Mándame un email a hola@wey.com"
pat = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
res = re.findall(pat, texto)
print(res)  # ['hola@wey.com']
