import pandas as pd

print("=== INICIO DEL PROCESO DE DATA WRANGLING ===")

# ===============================
# 1. CARGA Y EXPLORACIÓN DE DATOS
# ===============================

print("\nCargando datos...")
df = pd.read_csv(r"C:\Users\Wilson\Desktop\Curso Ciencia de Datos\BootcampWorkspace\Modulo3\Tarea Data wrangling\datos_financieros.csv")

print("\nVista previa:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nFilas duplicadas:", df.duplicated().sum())

# ===============================
# 2. LIMPIEZA Y TRANSFORMACIÓN
# ===============================

print("\nLimpiando datos...")

# Imputación de valores nulos
if df["Edad"].isnull().sum() > 0:
    df["Edad"] = df["Edad"].fillna(df["Edad"].median())

if df["Ingresos"].isnull().sum() > 0:
    df["Ingresos"] = df["Ingresos"].fillna(df["Ingresos"].mean())

if df["Ciudad"].isnull().sum() > 0:
    df["Ciudad"] = df["Ciudad"].fillna(df["Ciudad"].mode()[0])

# Eliminar duplicados
df = df.drop_duplicates()

# Convertir variables categóricas a numéricas
df["Genero"] = df["Genero"].map({"Masculino": 0, "Femenino": 1})

# ===============================
# 3. OPTIMIZACIÓN Y ESTRUCTURACIÓN
# ===============================

print("\nAplicando transformaciones...")

# Agrupación
resumen = df.groupby("Ciudad").agg({
    "Ingresos": "mean",
    "Edad": "mean"
})

print("\nResumen por ciudad:")
print(resumen)

# Filtrado
df_altos_ingresos = df[df["Ingresos"] > df["Ingresos"].mean()]

# Renombrar columnas
df = df.rename(columns={
    "Nombre": "Nombre_Cliente",
    "Edad": "Edad_Años",
    "Ingresos": "Ingresos_Mensuales"
})

# Reordenar columnas
df = df[["Nombre_Cliente", "Edad_Años", "Genero", "Ciudad", "Ingresos_Mensuales"]]

# ===============================
# 4. EXPORTACIÓN
# ===============================

print("\nGuardando archivos...")

df.to_csv("datos_limpios.csv", index=False)
df.to_excel("datos_limpios.xlsx", index=False)

print("\n=== PROCESO FINALIZADO ===")
print("Archivos generados: datos_limpios.csv y datos_limpios.xlsx")

print("\nVista final del dataset limpio:")
print(df.head())
