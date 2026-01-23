import pandas as pd
import requests
from io import StringIO

print("=== INICIO DEL PROCESO ===")

# ===============================
# 1. CARGA DE DATOS
# ===============================

# CSV
print("Cargando CSV...")
df_csv = pd.read_csv(r"C:\Users\Wilson\Desktop\Curso Ciencia de Datos\BootcampWorkspace\Modulo3\Clase3\datos.csv")

# Excel
print("Cargando Excel...")
df_excel = pd.read_excel(r"C:\Users\Wilson\Desktop\Curso Ciencia de Datos\BootcampWorkspace\Modulo3\Clase3\datos.xlsx")

# Web (Wikipedia)
print("Cargando tabla web...")

url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(PPA)_per_c%C3%A1pita"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "es-ES,es;q=0.9"
}

html = requests.get(url, headers=headers, timeout=30).text
tablas = pd.read_html(StringIO(html))

df_web = tablas[0]

print("Datos cargados correctamente.")

# ===============================
# 2. LIMPIEZA DE DATOS
# ===============================

print("Limpiando datos...")

# Unificamos los 3 DataFrames
df = pd.concat([df_csv, df_excel], ignore_index=True)

# Eliminamos duplicados
df = df.drop_duplicates()

# Eliminamos filas con valores nulos
df = df.dropna()

# ===============================
# 3. TRANSFORMACIÓN
# ===============================

print("Transformando datos...")

# Renombramos columnas para mejorar legibilidad
df = df.rename(columns={
    df.columns[0]: "Nombre",
    df.columns[1]: "Edad",
    df.columns[2]: "Ciudad"
})

# Ordenamos por Nombre
df = df.sort_values(by="Nombre")

# ===============================
# 4. EXPORTACIÓN
# ===============================

print("Guardando resultados...")

df.to_csv("resultado_limpio.csv", index=False)
df.to_excel("resultado_limpio.xlsx", index=False)

print("=== PROCESO FINALIZADO ===")
print("Archivo generado: resultado_limpio.csv y resultado_limpio.xlsx")

print("\nVista previa del resultado:")
print(df.head())