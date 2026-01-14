import numpy as np 

# 1) Crear matriz X (características) y vector Y (etiquetas)
#    Ejemplo: regresión lineal simple con intercepto (bias)
x = np.array([1, 2, 3, 4, 5], dtype=float)

# Construimos X con una columna de 1s (intercepto) y la variable x
X = np.column_stack([np.ones_like(x), x])  # forma (n, 2)

# Simulamos y = 2 + 3x
y = 2 + 3 * x
print(x)
print(X)
print(y)