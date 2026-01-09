'''Ejercicio Avanzado: Sistema de Gestión de Estudiantes

Objetivo:
Crear un programa que gestione estudiantes y becados, calcule estadísticas, permita buscar, filtrar y guardar datos en un archivo. Todo usando Python de forma avanzada.

💻 Código completo'''

from abc import ABC, abstractmethod

# --- Clases y Herencia ---
class Estudiante(ABC):
    def __init__(self, nombre, curso, nota):
        self.__nombre = nombre      # atributo privado
        self.__curso = curso
        self.__nota = nota
    
    # Getters y setters (encapsulamiento)
    def get_nombre(self):
        return self.__nombre
    
    def get_curso(self):
        return self.__curso
    
    def get_nota(self):
        return self.__nota
    
    def set_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 10:
            self.__nota = nueva_nota
    
    @abstractmethod
    def mostrar_info(self):
        pass

class AlumnoNormal(Estudiante):
    def mostrar_info(self):  # polimorfismo
        print(f"{self.get_nombre()} | Curso: {self.get_curso()} | Nota: {self.get_nota()}")

class AlumnoBecado(Estudiante):
    def __init__(self, nombre, curso, nota, beca):
        super().__init__(nombre, curso, nota)
        self.__beca = beca
    
    def mostrar_info(self):
        print(f"{self.get_nombre()} | Curso: {self.get_curso()} | Nota: {self.get_nota()} | Beca: {self.__beca}")

# --- Lista de estudiantes ---
alumnos = [
    AlumnoNormal("Ana", "1A", 8),
    AlumnoNormal("Luis", "1B", 6),
    AlumnoBecado("María", "1A", 9, True)
]

# --- Funciones auxiliares ---
def mostrar_estudiantes(lista):
    for alumno in lista:
        alumno.mostrar_info()
    print()

def promedio_notas(lista):
    return sum(a.get_nota() for a in lista) / len(lista)

# Generador para filtrar estudiantes
def estudiantes_altos(lista, minimo):
    for a in lista:
        if a.get_nota() >= minimo:
            yield a

# Buscar estudiante por nombre usando diccionario
def buscar_estudiante(lista, nombre):
    # Convertimos a diccionario temporal para usar items()
    for idx, alumno in enumerate(lista):
        info = {"nombre": alumno.get_nombre(), "curso": alumno.get_curso(), "nota": alumno.get_nota()}
        if info["nombre"].lower() == nombre.lower():
            return alumno
    return None

# Guardar estudiantes en archivo
def guardar_estudiantes(lista, archivo="alumnos.txt"):
    with open(archivo, "w") as f:
        for a in lista:
            f.write(f"{a.get_nombre()},{a.get_curso()},{a.get_nota()}\n")

# --- Programa Principal ---
print("=== Lista de Estudiantes ===")
mostrar_estudiantes(alumnos)

print("Promedio general:", promedio_notas(alumnos))

# Ordenar por nota descendente usando lambda
alumnos.sort(key=lambda x: x.get_nota(), reverse=True)
print("\n=== Estudiantes Ordenados por Nota ===")
mostrar_estudiantes(alumnos)

# Filtrar estudiantes con nota >= 8 usando yield
print("=== Estudiantes con Nota >= 8 ===")
for a in estudiantes_altos(alumnos, 8):
    a.mostrar_info()

# Buscar estudiante por nombre
nombre_buscar = input("\nIngrese el nombre del estudiante a buscar: ")
encontrado = buscar_estudiante(alumnos, nombre_buscar)
if encontrado:
    print("Estudiante encontrado:")
    encontrado.mostrar_info()
else:
    print("No se encontró al estudiante.")

# Agregar un nuevo estudiante
nombre = input("\nNombre del nuevo estudiante: ")
curso = input("Curso: ")
nota = float(input("Nota: "))
tipo = input("¿Es becado? (si/no): ").lower()
if tipo == "si":
    beca = True
    nuevo = AlumnoBecado(nombre, curso, nota, beca)
else:
    nuevo = AlumnoNormal(nombre, curso, nota)
alumnos.append(nuevo)

print("\n=== Lista Actualizada ===")
mostrar_estudiantes(alumnos)

# Guardar estudiantes en archivo
guardar_estudiantes(alumnos)
print("Datos guardados en 'alumnos.txt'")

'''✅ Conceptos que cubre este ejercicio
Concepto	Ejemplo en el código
Variables y tipos de datos	nombre, nota, curso
Listas	alumnos = [...]
Diccionarios	info = {"nombre": ..., "curso": ..., "nota": ...}
Bucles	for alumno in lista:
Condicionales	if a.get_nota() >= minimo:
Funciones	def promedio_notas(lista):
Generadores	yield en estudiantes_altos
Clases y Objetos	class AlumnoNormal(Estudiante):
Atributos privados	self.__nombre (encapsulamiento)
Getters y Setters	get_nombre(), set_nota()
Herencia	AlumnoBecado hereda de Estudiante
Polimorfismo	mostrar_info() redefinido en subclase
Ordenamiento	alumnos.sort(key=lambda x: x.get_nota(), reverse=True)
Entrada/Salida	input(), print()
Manejo de archivos	open(), write()
Funciones lambda	lambda x: x.get_nota()
Uso de items()	Diccionario temporal en buscar_estudiante()'''