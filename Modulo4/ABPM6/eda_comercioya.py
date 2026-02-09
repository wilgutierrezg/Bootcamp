#Lección 1: IDA + tipos de variables

import os
import pandas as pd

base_path = r"C:\Users\Wilson\Desktop\Curso Ciencia de Datos\BootcampWorkspace\Modulo4\ABPM6"
os.chdir(base_path)
ruta_csv = os.path.join(base_path, "dataset_comercioya.csv")

df = pd.read_csv(ruta_csv)

print(df.head())
print(df.info())
print(df.describe())

print("\nValores nulos:")
print(df.isnull().sum())

#Lección 2: Estadística descriptiva + histogramas + boxplot

import seaborn as sns
import matplotlib.pyplot as plt

print("Media:\n", df.mean(numeric_only=True))
print("Mediana:\n", df.median(numeric_only=True))
print("Desviación estándar:\n", df.std(numeric_only=True))

# Histograma
sns.histplot(df["monto_compra"], kde=True)
plt.title("Distribución del monto de compra")
plt.savefig("histplot.png")
plt.show()
plt.close()

# Boxplot (outliers)
sns.boxplot(x=df["monto_compra"])
plt.title("Outliers en monto de compra")
plt.savefig("boxplot.png")
plt.show()
plt.close()

#Lección 3: Correlación
corr = df.corr(numeric_only=True)
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.savefig("heatmap.png")
plt.show()
plt.close()

sns.scatterplot(x="visitas_web", y="monto_compra", data=df)
plt.title("Visitas vs Monto de compra")
plt.savefig("scatterplot.png")
plt.show()
plt.close()

#Lección 4: Regresión lineal (statsmodels)

import statsmodels.api as sm

X = df[["visitas_web", "reseñas"]]
y = df["monto_compra"]

X = sm.add_constant(X)

modelo = sm.OLS(y, X).fit()
print(modelo.summary())

#Lección 5: Visualizaciones avanzadas Seaborn

sns.pairplot(df)
plt.show()

sns.violinplot(x="categoria_cliente", y="monto_compra", data=df)
plt.savefig("violinplot.png")
plt.show()
plt.close()

sns.jointplot(x="visitas_web", y="monto_compra", data=df, kind="reg")
plt.show()

#Lección 6: Matplotlib personalizado
plt.figure(figsize=(10,5))
plt.plot(df["monto_compra"])
plt.title("Montos de compra en el tiempo")
plt.xlabel("Registro")
plt.ylabel("Monto")
plt.show()
