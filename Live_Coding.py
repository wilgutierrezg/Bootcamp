

class Persona:
    def __init__(self, nombre, edad, altura, rutina_completa, caloriasxdia):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.rutina_completa = rutina_completa
        self.caloriasxdia = caloriasxdia

personas=[]

def persona():
    nombre= str(input("nombre:"))
    edad= int(input("edad:"))
    altura= float(input("altura"))
    rutina_completa= str(input("siono:"))
    caloriasxdia=[]
    for i in range(5):
        valor= int(input(f"ingrese calorias{i+1:}"))
        caloriasxdia.append(valor)
    p = Persona(nombre, edad, altura, rutina_completa, caloriasxdia)
    personas.append(p)  

for i in range(int(input())):
    persona()
    print("\nNombres de las personas:")

while True:
    persona()  # Llamamos a la función para crear una persona
    
    continuar = input("¿Desea agregar otra persona? (s/n): ").lower()
    if continuar != "s":
        break  # Sale del bucle si el usuario no quiere seguir    

for persona in personas:
    print(persona.nombre)

#promediocal =sum(caloriasxdia)/len(caloriasxdia)
#personas.append(persona())
#for nombre in personas:
#   print(persona.nombre)


"""print(personas.nombre)
print(edad)
print(caloriasxdia)
print(prersonas)"""
#print(promediocal)