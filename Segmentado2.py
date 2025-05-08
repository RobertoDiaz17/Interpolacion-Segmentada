import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de distribución de temperatura en el cilindro (extraídos de la Tabla 2)
distancia = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
temperatura = np.array([250, 220, 180, 150, 130, 125])

# Realizar interpolación lineal
lineal_interp = interp1d(distancia, temperatura, kind='linear')

# Realizar interpolación cuadrática
cuadratica_interp = interp1d(distancia, temperatura, kind='quadratic')

# Realizar interpolación cúbica
cubica_interp = interp1d(distancia, temperatura, kind='cubic')

# Generar puntos para graficar las curvas interpoladas
distancia_interp = np.linspace(distancia.min(), distancia.max(), 100)
temperatura_lineal = lineal_interp(distancia_interp)
temperatura_cuadratica = cuadratica_interp(distancia_interp)
temperatura_cubica = cubica_interp(distancia_interp)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(distancia, temperatura, color='red', label='Datos Experimentales')
plt.plot(distancia_interp, temperatura_lineal, '--', color='blue', label='Interpolación Lineal')
plt.plot(distancia_interp, temperatura_cuadratica, '-.', color='green', label='Interpolación Cuadrática')
plt.plot(distancia_interp, temperatura_cubica, color='purple', label='Interpolación Cúbica')
plt.xlabel('Distancia (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Variación de Temperatura en un Motor')
plt.legend()
plt.grid(True)
plt.savefig('temperatura_motor_interpolacion.png')
plt.show()

# Comparación de la precisión (estimar temperatura en puntos intermedios)
print("Estimación de temperatura en puntos intermedios:")
puntos_intermedios = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
print("Distancia (cm) | Lineal (°C) | Cuadrática (°C) | Cúbica (°C)")
print("-------------------------------------------------------")
for x in puntos_intermedios:
    print(f"{x:.1f}            | {lineal_interp(x):.2f}         | {cuadratica_interp(x):.2f}           | {cubica_interp(x):.2f}")

# Discusión sobre el método que proporciona la mejor aproximación
print("\nDiscusión sobre el método de mejor aproximación:")
print("Observando la gráfica, la temperatura parece disminuir de manera relativamente suave a lo largo del cilindro")