'''Ejercicio: Sistema de gestión de estudiantes

Descripción:
Crea un programa que permita gestionar estudiantes y calcular estadísticas de notas, usando clases, métodos, atributos y listas. Debe permitir:

Crear estudiantes con nombre, curso y nota.

Mostrar todos los estudiantes.

Calcular el promedio de notas.

Ordenar estudiantes por nota de forma descendente.

Mostrar estudiantes con nota mayor a un valor dado.

Utilizar herencia para crear un tipo especial de estudiante “Becado” que tenga un atributo adicional beca.'''

#💻 Solución en Python

# --- Definición de clases y herencia ---
class Estudiante:
    def __init__(self, nombre, curso, nota):
        self.nombre = nombre     # atributo
        self.curso = curso       # atributo
        self.nota = nota         # atributo
    
    def mostrar_info(self):      # método
        print(f"{self.nombre} | Curso: {self.curso} | Nota: {self.nota}")

class EstudianteBecado(Estudiante):  # herencia
    def __init__(self, nombre, curso, nota, beca):
        super().__init__(nombre, curso, nota)
        self.beca = beca       # atributo adicional
    
    def mostrar_info(self):    # polimorfismo: redefinición del método
        print(f"{self.nombre} | Curso: {self.curso} | Nota: {self.nota} | Beca: {self.beca}")

# --- Lista de estudiantes ---
alumnos = [
    Estudiante("Ana", "1A", 8),
    Estudiante("Luis", "1B", 6),
    EstudianteBecado("María", "1A", 9, True)
]

# --- Función para mostrar todos los estudiantes ---
def mostrar_estudiantes(lista):
    for alumno in lista:
        alumno.mostrar_info()  # usa métodos de cada objeto
    print()

# --- Función para calcular promedio ---
def promedio_notas(lista):
    suma = 0
    for alumno in lista:
        suma += alumno.nota
    return suma / len(lista)

# --- Función generadora para estudiantes con nota alta ---
def estudiantes_altas(lista, minimo):
    for alumno in lista:
        if alumno.nota >= minimo:
            yield alumno

# --- Programa principal ---
print("=== Lista de Estudiantes ===")
mostrar_estudiantes(alumnos)

print("Promedio de notas:", promedio_notas(alumnos))
print()

# Ordenar por nota descendente
alumnos.sort(key=lambda x: x.nota, reverse=True)
print("=== Estudiantes Ordenados por Nota (descendente) ===")
mostrar_estudiantes(alumnos)

# Filtrar estudiantes con nota >= 8 usando yield
print("=== Estudiantes con nota >= 8 ===")
for a in estudiantes_altas(alumnos, 8):
    a.mostrar_info()

# Agregar un nuevo estudiante desde input
print()
nombre = input("Ingrese nombre del nuevo estudiante: ")
curso = input("Ingrese curso: ")
nota = float(input("Ingrese nota: "))
alumnos.append(Estudiante(nombre, curso, nota))
print("\n=== Lista Actualizada de Estudiantes ===")
mostrar_estudiantes(alumnos)

'''✅ Qué conceptos de Python incluye:
Concepto	Ejemplo en el código
Variables	nombre, curso, nota
Tipos de datos	str, int, float, bool
Listas	alumnos = [...]
Diccionarios	Podrías agregar uno para estadísticas, aunque aquí usamos atributos
Bucles	for alumno in lista:
Condicionales	if alumno.nota >= minimo:
Funciones	def mostrar_estudiantes(lista):
Generadores	yield en estudiantes_altas
Clases	class Estudiante:
Objetos	Estudiante("Ana", "1A", 8)
Métodos	mostrar_info()
Atributos	self.nombre, self.nota
Herencia	class EstudianteBecado(Estudiante):
Polimorfismo	Redefinición de mostrar_info en EstudianteBecado
Ordenamiento	alumnos.sort(key=lambda x: x.nota, reverse=True)
Entrada/Salida	input(), print()'''