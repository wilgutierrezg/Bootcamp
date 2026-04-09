# =====================================
# PROYECTO: Reducción Dimensional - DataMed
# =====================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# =============================
# 1. DATASET SIMULADO (CLÍNICO)
# =============================
np.random.seed(42)

data = pd.DataFrame(np.random.rand(300, 100),
                    columns=[f'var_{i}' for i in range(100)])

# =============================
# 2. ESCALAMIENTO
# =============================
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# =============================
# 3. PCA
# =============================
pca = PCA()
pca.fit(data_scaled)

# Varianza explicada acumulada
varianza = np.cumsum(pca.explained_variance_ratio_)

plt.figure()
plt.plot(varianza)
plt.title("Varianza explicada acumulada - PCA")
plt.xlabel("Componentes")
plt.ylabel("Varianza acumulada")
plt.show()

# Elegimos 2 componentes para visualización
pca_2 = PCA(n_components=2)
pca_result = pca_2.fit_transform(data_scaled)

plt.figure()
plt.scatter(pca_result[:,0], pca_result[:,1])
plt.title("PCA - Visualización 2D")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# =============================
# 4. t-SNE
# =============================
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, max_iter=1000, random_state=42)
tsne_result = tsne.fit_transform(data_scaled)

plt.figure()
plt.scatter(tsne_result[:,0], tsne_result[:,1])
plt.title("t-SNE - Visualización 2D")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.show()