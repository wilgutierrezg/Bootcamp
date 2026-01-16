import pandas as pd
### Métodos básicos de exploración 
import pandas as pd
from pathlib import Path

# --- Cargar CSV (misma carpeta que este .py) ---
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "Titanic-Dataset.csv"

df = pd.read_csv(csv_path)

# head() – primeras filas del DataFrame
# Sirve para tener una primera mirada rápida: columnas, tipos de datos “a ojo”, valores faltantes evidentes.
df.head()
df.head(3)

# tail() – últimas filas del DataFrame
# Útil para revisar el final del dataset (a veces hay datos raros al final, o simplemente para confirmar el tamaño).
df.tail()
df.tail(3)

# info() – estructura del DataFrame
# Este es clave pedagógicamente. Aquí se responde:
# ¿Cuántas filas y columnas hay?
# ¿Qué tipo de dato tiene cada columna?
# ¿Hay valores nulos?
df.info()

