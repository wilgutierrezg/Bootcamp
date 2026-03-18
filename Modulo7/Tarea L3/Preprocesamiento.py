import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler

# -----------------------------
# 1. Crear dataset inicial
# -----------------------------
data = {
    "ID": [1, 2, 3, 4],
    "Edad": [25, 45, 30, 40],
    "Ciudad": ["Madrid", "Sevilla", "Madrid", "Barcelona"],
    "Ingresos": [30000, 50000, np.nan, 40000]
}

df = pd.DataFrame(data)

print("=== DATASET ORIGINAL ===")
print(df)


# -----------------------------
# 2. Imputar valores faltantes
# -----------------------------
media_ingresos = df["Ingresos"].mean()
df["Ingresos"].fillna(media_ingresos, inplace=True)

print("\n=== DATASET CON IMPUTACIÓN ===")
print(df)


# -----------------------------
# 3. Label Encoding
# -----------------------------
le = LabelEncoder()
df["Ciudad_Label"] = le.fit_transform(df["Ciudad"])

print("\n=== CON LABEL ENCODING ===")
print(df)


# -----------------------------
# 4. One-Hot Encoding (Dummies)
# -----------------------------
dummies = pd.get_dummies(df["Ciudad"], prefix="Ciudad")
df = pd.concat([df, dummies], axis=1)

print("\n=== CON VARIABLES DUMMY ===")
print(df)


# -----------------------------
# 5. Escalamiento Min-Max
# -----------------------------
scaler_minmax = MinMaxScaler()
df[["Edad_MinMax", "Ingresos_MinMax"]] = scaler_minmax.fit_transform(df[["Edad", "Ingresos"]])

print("\n=== NORMALIZACIÓN MIN-MAX ===")
print(df[["Edad_MinMax", "Ingresos_MinMax"]])


# -----------------------------
# 6. Estandarización Z-Score
# -----------------------------
scaler_standard = StandardScaler()
df[["Edad_Zscore", "Ingresos_Zscore"]] = scaler_standard.fit_transform(df[["Edad", "Ingresos"]])

print("\n=== ESTANDARIZACIÓN Z-SCORE ===")
print(df[["Edad_Zscore", "Ingresos_Zscore"]])


# -----------------------------
# 7. Guardar dataset final
# -----------------------------
df.to_csv("dataset_preprocesado.csv", index=False)

print("\n✅ Dataset guardado como 'dataset_preprocesado.csv'")


# -----------------------------
# 8. Mostrar dataset final
# -----------------------------
print("\n=== DATASET FINAL ===")
print(df)