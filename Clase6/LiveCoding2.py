# --- DATOS INICIALES ---
nombres = ["Ana", "Juan", "Maria", "Pedro", "Luis"]
notas = [85, 42, 90, 55, 70]

# 1. Usar range(start, stop, step) para generar secuencias
print("--- 1. Generando secuencia de pasos ---")
for i in range(0, 10, 2):  # De 0 a 10 de 2 en 2
    print(f"Paso de auditoría: {i}")

# 2. Combinar listas con zip()
print("2) Construyendo registros con zip():")
registros = []
for nombre, notas in zip(nombres, notas):
    registros.append({
        "nombre": nombre,
        "notas": notas
    })

print(registros)

# 3. Crear diccionarios con comprensiones
print("\n--- 2 y 3. Mapeo de Estudiantes y Notas ---")
estudiantes_dict = {nombre: nota for nombre, nota in zip(nombres, notas)}
print(f"Diccionario creado: {estudiantes_dict}")


# 4. Usar enumerate() para recorrer con índice
print("\n--- 4. Listado Numerado de Estudiantes ---")
for idx, nombre in enumerate(nombres, start=1):
    print(f"{idx}. Estudiante: {nombre}")

# 6. Introducir un generador con yield para listar alumnos aprobados
def generador_aprobados(diccionario_notas):
    for nombre, nota in diccionario_notas.items():
        if nota >= 60:
            yield nombre, nota

# 5. Implementar break y continue dentro de un análisis de notas
# 7. Mostrar cómo depurar con impresión selectiva y condiciones
print("\n--- 5, 6 y 7. Informe de Rendimiento Académico ---")
print("Buscando alumnos aprobados...")

aprobados = generador_aprobados(estudiantes_dict)

for nombre, nota in aprobados:
    # Ejemplo de depuración selectiva (Punto 7)
    if nota > 80:
        print(f"[DESTACADO] {nombre} tiene una excelente nota: {nota}")
    
    # Ejemplo de continue: Si es Maria, saltamos su impresión detallada
    if nombre == "Maria":
        print("(Saltando detalle de Maria por privacidad)")
        continue
    
    print(f"Procesando informe para: {nombre}")
    
    # Ejemplo de break: Detener si encontramos a alguien específico
    if nombre == "Luis":
        print("Se alcanzó el límite de revisión. Finalizando.")
        break