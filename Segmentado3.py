import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de consumo de combustible (extraídos de la Tabla 3)
velocidad = np.array([40, 60, 80, 100, 120, 140])
consumo = np.array([6.5, 5.8, 5.5, 5.7, 6.2, 7.0])

# Realizar interpolación lineal
lineal_interp = interp1d(velocidad, consumo, kind='linear')

# Realizar interpolación cuadrática
cuadratica_interp = interp1d(velocidad, consumo, kind='quadratic')

# Realizar interpolación cúbica
cubica_interp = interp1d(velocidad, consumo, kind='cubic')

# Generar puntos para graficar las curvas interpoladas
velocidad_interp = np.linspace(velocidad.min(), velocidad.max(), 100)
consumo_lineal = lineal_interp(velocidad_interp)
consumo_cuadratica = cuadratica_interp(velocidad_interp)
consumo_cubica = cubica_interp(velocidad_interp)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(velocidad, consumo, color='red', label='Datos Experimentales')
plt.plot(velocidad_interp, consumo_lineal, '--', color='blue', label='Interpolación Lineal')
plt.plot(velocidad_interp, consumo_cuadratica, '-.', color='green', label='Interpolación Cuadrática')
plt.plot(velocidad_interp, consumo_cubica, color='purple', label='Interpolación Cúbica')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Consumo (L/100 km)')
plt.title('Ajuste de la Curva de Consumo de Combustible')
plt.legend()
plt.grid(True)
plt.savefig('consumo_combustible_interpolacion.png')
plt.show()

# Determinar intervalos de comportamiento lineal y curvo (aproximación visual)
print("Análisis de intervalos de comportamiento:")
print("Observando los datos y la gráfica:")
print("- Intervalo de 60 a 80 km/h: El consumo parece tener una disminución casi lineal.")
print("- Intervalos")