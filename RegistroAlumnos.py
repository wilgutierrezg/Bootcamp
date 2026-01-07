# 1. Crear la lista llamada alumnos con diccionarios
alumnos = [
    {"nombre": "Ana", "curso": "1A", "nota": 8},
    {"nombre": "Luis", "curso": "1B", "nota": 6},
    {"nombre": "María", "curso": "1A", "nota": 9}
]

# 2 y 3. Mostrar todos los nombres usando un bucle for
print("Lista de alumnos:")
for alumno in alumnos:
    print(alumno["nombre"])

# 4. Agregar un nuevo alumno al final de la lista
nuevo_alumno = {"nombre": "Carlos", "curso": "1C", "nota": 7}
alumnos.append(nuevo_alumno)

# 5. Modificar la nota del segundo alumno (índice 1)
alumnos[1]["nota"] = 8

# 6. Calcular y mostrar el promedio general de las notas
suma_notas = 0
for alumno in alumnos:
    suma_notas += alumno["nota"]

promedio = suma_notas / len(alumnos)
print("Promedio general de notas:", promedio)

# 7. Ordenar la lista por nota de forma descendente
alumnos.sort(key=lambda x: x["nota"], reverse=True)

# Mostrar la lista ordenada
print("\nLista de alumnos ordenada por nota (descendente):")
for alumno in alumnos:
    print(alumno)