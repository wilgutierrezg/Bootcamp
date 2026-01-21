import numpy as np

# 1️⃣ Crear datos simulados: precios de 5 acciones durante 5 días
datos = np.array([
    [100, 102, 101, 103, 105],
    [50, 51, 49, 52, 54],
    [200, 198, 202, 205, 207],
    [80, 79, 81, 82, 83],
    [120, 121, 119, 122, 124]
])

print("Matriz de datos:\n", datos)

# 2️⃣ Análisis estadístico por acción (por filas)
promedios = np.mean(datos, axis=1)
maximos = np.max(datos, axis=1)
minimos = np.min(datos, axis=1)

print("\nPromedios por acción:", promedios)
print("Máximos por acción:", maximos)
print("Mínimos por acción:", minimos)

# 3️⃣ Variación porcentual diaria
variacion = (datos[:, 1:] - datos[:, :-1]) / datos[:, :-1] * 100
print("\nVariación porcentual diaria:\n", variacion)

# 4️⃣ Aplicar funciones matemáticas
logaritmo = np.log(datos)
normalizado = (datos - np.min(datos)) / (np.max(datos) - np.min(datos))

print("\nLogaritmo de los datos:\n", logaritmo)
print("\nDatos normalizados:\n", normalizado)

# 5️⃣ Indexación avanzada: precio de la acción 3 en el día 4
valor_especifico = datos[2, 3]
print("\nPrecio de la acción 3 en el día 4:", valor_especifico)

# 6️⃣ Broadcasting: aumentar todos los precios un 5%
aumento = datos * 1.05
print("\nPrecios con aumento del 5%:\n", aumento)