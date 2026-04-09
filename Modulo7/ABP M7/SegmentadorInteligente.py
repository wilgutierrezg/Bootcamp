# =============================================
# PROYECTO: Segmentador Inteligente de Clientes
# Módulo 7 - Machine Learning No Supervisado
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# =============================
# 1. DATASET SIMULADO
# =============================
np.random.seed(42)

data = pd.DataFrame({
    'edad': np.random.randint(18, 70, 300),
    'ingresos': np.random.randint(1000, 10000, 300),
    'gasto_anual': np.random.randint(500, 15000, 300),
    'frecuencia_compra': np.random.randint(1, 50, 300)
})

# =============================
# 2. PREPROCESAMIENTO
# =============================
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# =============================
# 3. REDUCCIÓN DIMENSIONAL
# =============================

# PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(data_scaled)

plt.figure()
plt.scatter(pca_data[:,0], pca_data[:,1])
plt.title('PCA - Clientes')
plt.show()

# t-SNE
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, max_iter=1000, random_state=42)
tsne_data = tsne.fit_transform(data_scaled)

plt.figure()
plt.scatter(tsne_data[:,0], tsne_data[:,1])
plt.title('t-SNE - Clientes')
plt.show()

# =============================
# 4. K-MEANS
# =============================

# Método del codo
inertia = []
K = range(1,10)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

plt.figure()
plt.plot(K, inertia)
plt.title('Método del codo')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.show()

# K óptimo = 3 (ejemplo)
kmeans = KMeans(n_clusters=3, random_state=42)
labels_k = kmeans.fit_predict(data_scaled)

print("Silhouette KMeans:", silhouette_score(data_scaled, labels_k))

# =============================
# 5. DBSCAN
# =============================

dbscan = DBSCAN(eps=0.8, min_samples=5)
labels_db = dbscan.fit_predict(data_scaled)

# Filtrar ruido (-1)
if len(set(labels_db)) > 1:
    print("Silhouette DBSCAN:", silhouette_score(data_scaled, labels_db))

# =============================
# 6. JERÁRQUICO
# =============================

agg = AgglomerativeClustering(n_clusters=3)
labels_agg = agg.fit_predict(data_scaled)

print("Silhouette Jerárquico:", silhouette_score(data_scaled, labels_agg))

# =============================
# 7. VISUALIZACIÓN FINAL
# =============================

plt.figure()
plt.scatter(pca_data[:,0], pca_data[:,1], c=labels_k)
plt.title('Clusters KMeans (PCA)')
plt.show()

plt.figure()
plt.scatter(pca_data[:,0], pca_data[:,1], c=labels_agg)
plt.title('Clusters Jerárquico (PCA)')
plt.show()

plt.figure()
plt.scatter(pca_data[:,0], pca_data[:,1], c=labels_db)
plt.title('Clusters DBSCAN (PCA)')
plt.show()

# =============================
# 8. CONCLUSIÓN
# =============================
print("KMeans ofrece clusters más estables y fáciles de interpretar.")
