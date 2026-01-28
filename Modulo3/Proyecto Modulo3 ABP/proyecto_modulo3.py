import pandas as pd
import numpy as np
import requests
from io import StringIO

print("=== PROYECTO PREPARACIÓN DE DATOS - MODULO 3 ===")

# ===============================
# 1. CARGA DE DATOS
# ===============================

base_path = r"C:\Users\Wilson\Desktop\Curso Ciencia de Datos\BootcampWorkspace\Modulo3\Proyecto Modulo3 ABP"

print("Cargando CSV...")
df_csv = pd.read_csv(base_path + r"\clientes_ecommerce.csv", encoding="latin1")

print("Cargando Excel...")
df_excel = pd.read_excel(base_path + r"\clientes_ecommerce.xlsx")

print("Cargando tabla web...")

url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(PPA)_per_c%C3%A1pita"
headers = {"User-Agent": "Mozilla/5.0"}

html = requests.get(url, headers=headers, timeout=30).text
tablas = pd.read_html(StringIO(html))
df_web = tablas[0]

print("Datos cargados correctamente.")

# ===============================
# 2. UNIFICACIÓN
# ===============================

df_clientes = pd.concat([df_csv, df_excel], ignore_index=True)

print("Shape unificado:", df_clientes.shape)

# ===============================
# 3. LIMPIEZA
# ===============================

print("Limpiando datos...")

# Eliminar duplicados
df_clientes = df_clientes.drop_duplicates()

# Rellenar nulos
for col in df_clientes.select_dtypes(include="number").columns:
    df_clientes[col] = df_clientes[col].fillna(df_clientes[col].mean())

for col in df_clientes.select_dtypes(include="object").columns:
    df_clientes[col] = df_clientes[col].fillna("Desconocido")

# ===============================
# 4. OUTLIERS (IQR)
# ===============================

print("Tratando outliers...")

for col in df_clientes.select_dtypes(include="number").columns:
    Q1 = df_clientes[col].quantile(0.25)
    Q3 = df_clientes[col].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR

    df_clientes[col] = np.where(
        df_clientes[col] < lim_inf, lim_inf,
        np.where(df_clientes[col] > lim_sup, lim_sup, df_clientes[col])
    )

# ===============================
# 5. DATA WRANGLING
# ===============================

print("Aplicando wrangling...")

# Crear columna calculada si existe monto
if "monto" in df_clientes.columns:
    df_clientes["monto_log"] = np.log1p(df_clientes["monto"])

# Convertir columnas de texto a mayúsculas
for col in df_clientes.select_dtypes(include="object").columns:
    df_clientes[col] = df_clientes[col].str.upper()

# ===============================
# 6. AGRUPAMIENTO
# ===============================

print("Agrupando datos...")

if "ciudad" in df_clientes.columns and "monto" in df_clientes.columns:
    resumen = df_clientes.groupby("ciudad")["monto"].mean().reset_index()
    resumen.to_csv(base_path + r"\resumen_por_ciudad.csv", index=False)

# ===============================
# 7. PIVOT Y MELT
# ===============================

if "ciudad" in df_clientes.columns and "categoria" in df_clientes.columns and "monto" in df_clientes.columns:
    tabla_pivot = df_clientes.pivot_table(
        values="monto",
        index="ciudad",
        columns="categoria",
        aggfunc="mean"
    )

    tabla_pivot.to_excel(base_path + r"\tabla_pivot.xlsx")

    tabla_melt = tabla_pivot.reset_index().melt(id_vars="ciudad")
    tabla_melt.to_csv(base_path + r"\tabla_melt.csv", index=False)

# ===============================
# 8. EXPORTACIÓN FINAL
# ===============================

print("Exportando dataset final...")

df_clientes.to_csv(base_path + r"\dataset_final.csv", index=False)
df_clientes.to_excel(base_path + r"\dataset_final.xlsx", index=False)

print("=== PROCESO FINALIZADO ===")
print("Archivos generados:")
print(" - dataset_final.csv")
print(" - dataset_final.xlsx")
print(" - resumen_por_ciudad.csv")
print(" - tabla_pivot.xlsx")
print(" - tabla_melt.csv")