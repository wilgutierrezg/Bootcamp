import numpy as np

data= np.random.rand(10,3)
print(data)

mean_col = np.mean(data,axis=0)
print(mean_col)

std_col= np.std(data,axis=0)
print(std_col)

data_scaled=(data-mean_col)/std_col

promedio_primera_col= mean_col[0]
filtrar_data=data[data[:,0]>promedio_primera_col]
print(filtrar_data)

mean_row=np.mean(data,axis=1).reshape(-1,1)
data_with_mean=np.hstack((data,mean_row))
print(mean_row)

matriz_correlacion=np.corrcoef(data,rowvar=false)
print(matriz_correlacion)
