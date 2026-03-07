
# ============================================
# Proyecto: Hábitos saludables en estudiantes
# Módulo: Inferencia Estadística
# ============================================

# 1 Importar librerías

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# 2 Cargar dataset

df = pd.read_csv("Modulo6/habitos_estudiantes.csv")

print("\nPrimeros registros del dataset:")
print(df.head())


# 3 Información general

print("\nInformación del dataset:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())


# ============================================
# 4 Análisis exploratorio (EDA)
# ============================================

# Distribución de horas de sueño

plt.figure()
plt.hist(df["horas_sueno"], bins=10)
plt.title("Distribución de horas de sueño")
plt.xlabel("Horas de sueño")
plt.ylabel("Frecuencia")
plt.show()


# Distribución de actividad física

plt.figure()
plt.hist(df["actividad_fisica"], bins=10)
plt.title("Distribución de actividad física semanal")
plt.xlabel("Minutos por semana")
plt.ylabel("Frecuencia")
plt.show()


# ============================================
# 5 Distribución de probabilidad
# ============================================

plt.figure()
sns.histplot(df["horas_sueno"], kde=True)
plt.title("Distribución de horas de sueño con KDE")
plt.show()


# ============================================
# 6 Teorema del Límite Central
# ============================================

medias = []

for i in range(1000):
    muestra = df["horas_sueno"].sample(30)
    medias.append(muestra.mean())

plt.figure()
plt.hist(medias, bins=30)
plt.title("Distribución de medias muestrales (TLC)")
plt.xlabel("Media muestral")
plt.ylabel("Frecuencia")
plt.show()


# ============================================
# 7 Intervalo de confianza
# ============================================

media = df["horas_sueno"].mean()
desv = df["horas_sueno"].std()
n = len(df)

intervalo = stats.t.interval(0.95, n-1, loc=media, scale=desv/np.sqrt(n))

print("\nIntervalo de confianza 95% para horas de sueño:")
print(intervalo)


# ============================================
# 8 Test de hipótesis
# ============================================

# H0: media >= 7 horas
# H1: media < 7 horas

t_stat, p_valor = stats.ttest_1samp(df["horas_sueno"], 7)

print("\nResultado del test de hipótesis:")
print("t-statistic:", t_stat)
print("p-valor:", p_valor)


# ============================================
# 9 Decisión estadística
# ============================================

alpha = 0.05

if p_valor < alpha:
    print("\nSe rechaza la hipótesis nula")
else:
    print("\nNo se rechaza la hipótesis nula")


# ============================================
# 10 Conclusión
# ============================================

print("\nConclusión:")
print("El análisis permite evaluar los hábitos de sueño en estudiantes y aplicar métodos de inferencia estadística.")