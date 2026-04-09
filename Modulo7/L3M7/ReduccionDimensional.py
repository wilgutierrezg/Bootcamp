# PROYECTO: Reducción Dimensional - VisionData
# Autor: [Tu Nombre]

# =============================
# 1. LIBRERÍAS
# =============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# =============================
# 2. GENERACIÓN DE DATASET SIMULADO
# =============================
np.random.seed(42)

data = pd.DataFrame(np.random.rand(300, 60), columns=[f'var_{i}' for i in range(60)])

# =============================
# 3. LIMPIEZA Y ESCALAMIENTO
# =============================
data = data.dropna()

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# =============================
# 4. PCA
# =============================
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data_scaled)

plt.figure()
plt.scatter(pca_result[:,0], pca_result[:,1])
plt.title('PCA - Reducción a 2D')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.show()

# =============================
# 5. t-SNE
# =============================
tsne = TSNE(n_components=2, random_state=42)
tsne_result = tsne.fit_transform(data_scaled)

plt.figure()
plt.scatter(tsne_result[:,0], tsne_result[:,1])
plt.title('t-SNE - Reducción a 2D')
plt.xlabel('Dim 1')
plt.ylabel('Dim 2')
plt.show()

# =============================
# 6. COMPARACIÓN
# =============================
print("Varianza explicada PCA:", pca.explained_variance_ratio_)

# =============================
# 7. CONCLUSIÓN
# =============================
print("PCA es más interpretable, t-SNE mejor para visualizar clusters.")
