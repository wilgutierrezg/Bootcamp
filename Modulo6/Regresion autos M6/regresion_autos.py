import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -----------------------------
# 1. Crear dataset
# -----------------------------
data = {
    "Antiguedad": [5, 3, 7, 2],
    "Kilometraje": [50000, 30000, 70000, 25000],
    "Puertas": [4, 2, 4, 2],
    "Precio": [12000, 15000, 9000, 16000]
}

df = pd.DataFrame(data)

print("=== DATASET ===")
print(df)

# -----------------------------
# 2. Variables
# -----------------------------
X = df[["Antiguedad", "Kilometraje", "Puertas"]]
y = df["Precio"]

# -----------------------------
# 3. División entrenamiento/prueba
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 4. Modelo
# -----------------------------
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# -----------------------------
# 5. Predicciones
# -----------------------------
y_pred = modelo.predict(X_test)

# -----------------------------
# 6. Métricas
# -----------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n=== MÉTRICAS ===")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

# -----------------------------
# 7. Gráfico
# -----------------------------
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Valores Reales")
plt.ylabel("Valores Predichos")
plt.title("Comparación: Reales vs Predichos")

# línea ideal
plt.plot([y.min(), y.max()], [y.min(), y.max()])

plt.savefig("grafico_regresion.png")
plt.show()