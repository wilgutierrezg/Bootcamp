# =============================================
# PROYECTO: Clasificador de Imágenes de Ropa
# Módulo 8 - Deep Learning
# =============================================

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.utils import to_categorical

# =============================
# 1. CARGA DE DATOS
# =============================
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Normalización
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encoding
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# =============================
# 2. MODELO DENSO
# =============================
model_dense = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model_dense.compile(optimizer='adam',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

history_dense = model_dense.fit(x_train, y_train_cat,
                                epochs=5,
                                validation_data=(x_test, y_test_cat))

# =============================
# 3. MODELO CNN
# =============================

# reshape para CNN
x_train_cnn = x_train.reshape(-1,28,28,1)
x_test_cnn = x_test.reshape(-1,28,28,1)

model_cnn = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])

model_cnn.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

history_cnn = model_cnn.fit(x_train_cnn, y_train_cat,
                            epochs=5,
                            validation_data=(x_test_cnn, y_test_cat))

# =============================
# 4. GRÁFICA DE ENTRENAMIENTO
# =============================
plt.figure()
plt.plot(history_cnn.history['accuracy'], label='Entrenamiento')
plt.plot(history_cnn.history['val_accuracy'], label='Validación')
plt.title('Precisión del modelo CNN')
plt.xlabel('Épocas')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# =============================
# 5. EVALUACIÓN
# =============================

loss_dense, acc_dense = model_dense.evaluate(x_test, y_test_cat)
loss_cnn, acc_cnn = model_cnn.evaluate(x_test_cnn, y_test_cat)

print("Accuracy Red Densa:", acc_dense)
print("Accuracy CNN:", acc_cnn)

# =============================
# 6. NOMBRES DE CLASES
# =============================
labels = [
    'Camiseta', 'Pantalón', 'Suéter', 'Vestido', 'Abrigo',
    'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Botín'
]

# =============================
# 7. PREDICCIÓN
# =============================

sample = x_test_cnn[0].reshape(1,28,28,1)
pred = model_cnn.predict(sample)

clase = np.argmax(pred)
print("Clase predicha:", labels[clase])

plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicción: {labels[clase]}")
plt.axis('off')
plt.show()
