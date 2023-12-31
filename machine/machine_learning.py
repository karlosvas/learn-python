import tensorflow as tf
import numpy as np


celsius = np.array([-40, -10, 0, 8, 15, 22 ,38], dtype=float)
fahrenheit = np.array([-40, -14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

# Nuevas capas intermedias
# oculta1 = tf.keras.layers.Dense(units= 3, input_shape=[1])
# oculta2 = tf.keras.layers.Dense(units= 3)
# salida = tf.keras.layers.Dense(units= 1)
# modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss= 'mean_squared_error'
)

print("Comenzando el entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

from matplotlib import pyplot as plt

plt.xlabel("#Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

plt.show()

print("Predicción:")
resultado = modelo.predict([100.0])
print(f"El resultado es {str(resultado)} fahrenheit")

## Accedemos a las variables que se hann  generado una vez la maquina ha sido entrenada.
print("Variables internas del modelo:")
print(modelo.get_weights())

# print(oculta1.get_weights())
# print(oculta2.get_weights())
# print(salida.get_weights())