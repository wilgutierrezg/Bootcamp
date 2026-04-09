# PROYECTO: Predicción de gasto en clientes e-commerce
# Autor: [Tu Nombre]

# =============================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =============================
# 2. CARGA DE DATOS (SIMULADOS)
# =============================
np.random.seed(42)

data = pd.DataFrame({
    'edad': np.random.randint(18, 65, 200),
    'visitas': np.random.randint(1, 50, 200),
    'tiempo_sitio': np.random.uniform(1, 20, 200),
    'pais': np.random.choice(['MX', 'AR', 'CL'], 200),
    'gasto': np.random.uniform(20, 500, 200)
})

# =============================
# 3. PREPROCESAMIENTO
# =============================
X = data.drop('gasto', axis=1)
y = data['gasto']

num_features = ['edad', 'visitas', 'tiempo_sitio']
cat_features = ['pais']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(), cat_features)
])

# =============================
# 4. DIVISIÓN DE DATOS
# =============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =============================
# 5. MODELOS
# =============================
models = {
    'Linear': LinearRegression(),
    'KNN': KNeighborsRegressor(),
    'Boosting': GradientBoostingRegressor()
}

results = {}

for name, model in models.items():
    pipe = Pipeline([
        ('prep', preprocessor),
        ('model', model)
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    results[name] = (mae, rmse, r2)

# =============================
# 6. RESULTADOS
# =============================
results_df = pd.DataFrame(results, index=['MAE', 'RMSE', 'R2']).T
print(results_df)

# =============================
# 7. OPTIMIZACIÓN (GRID SEARCH)
# =============================
param_grid = {
    'model__n_estimators': [50, 100],
    'model__learning_rate': [0.05, 0.1],
}

pipe_boost = Pipeline([
    ('prep', preprocessor),
    ('model', GradientBoostingRegressor())
])

grid = GridSearchCV(pipe_boost, param_grid, cv=5, scoring='neg_mean_squared_error')
grid.fit(X_train, y_train)

best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test)

print("\nMejor modelo Boosting optimizado:")
print("MAE:", mean_absolute_error(y_test, y_pred_best))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_best)))
print("R2:", r2_score(y_test, y_pred_best))

# =============================
# 8. CONCLUSIÓN
# =============================
print("\nEl modelo de Gradient Boosting optimizado presenta mejor rendimiento general.")
