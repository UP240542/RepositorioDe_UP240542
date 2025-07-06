dog = {}
dog['nombre'] = 'Rex'
dog['edad'] = 5
dog['raza'] = 'Labrador'
print(dog, len(dog))

student = {
    'first_name': 'Ana', 'last_name': 'Lopez',
    'edad': 22, 'skills': ['Python','SQL'], 'ciudad': 'CDMX'
}
print(student.keys(), student.values())
student['skills'].append('Django')
print(student['skills'])

items = list(student.items())
print(items)
del student['ciudad']
copy = student.copy()
student.clear()
print(student, copy)
