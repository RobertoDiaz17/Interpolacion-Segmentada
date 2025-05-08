import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import tkinter as tk
from tkinter import scrolledtext

# Datos de deflexión de la viga (extraídos de la Tabla 1)
longitud = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
deflexion = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])

# Realizar interpolación lineal
lineal_interp = interp1d(longitud, deflexion, kind='linear')

# Realizar interpolación cuadrática
cuadratica_interp = interp1d(longitud, deflexion, kind='quadratic')

# Realizar interpolación cúbica
cubica_interp = interp1d(longitud, deflexion, kind='cubic')

# Generar puntos para graficar las curvas interpoladas
longitud_interp = np.linspace(longitud.min(), longitud.max(), 100)
deflexion_lineal = lineal_interp(longitud_interp)
deflexion_cuadratica = cuadratica_interp(longitud_interp)
deflexion_cubica = cubica_interp(longitud_interp)

# Crear la ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Análisis de Deflexión de Viga")

# Crear un widget de texto con scrollbar para mostrar los resultados
texto_resultados = scrolledtext.ScrolledText(ventana, width=60, height=15)
texto_resultados.pack(padx=10, pady=10)

# Función para generar y mostrar los resultados en el widget de texto
def mostrar_resultados():
    texto_resultados.insert(tk.END, "Comparación de las aproximaciones en algunos puntos:\n")
    texto_resultados.insert(tk.END, "Longitud (m) | Lineal (mm) | Cuadrática (mm) | Cúbica (mm)\n")
    texto_resultados.insert(tk.END, "-------------------------------------------------------\n")
    puntos_comparacion = np.linspace(longitud.min(), longitud.max(), 5)
    for x in puntos_comparacion:
        texto_resultados.insert(tk.END, f"{x:.2f}         | {lineal_interp(x):.2f}         | {cuadratica_interp(x):.2f}           | {cubica_interp(x):.2f}\n")

    texto_resultados.insert(tk.END, "\nAnálisis del método más adecuado:\n")
    texto_resultados.insert(tk.END, "Observando la gráfica, la interpolación cúbica parece generar una curva más suave que conecta los puntos experimentales de manera más natural.\n")
    texto_resultados.insert(tk.END, "La interpolación lineal conecta los puntos con líneas rectas, lo cual puede no representar con precisión el comportamiento real de la deflexión de la viga.\n")
    texto_resultados.insert(tk.END, "La interpolación cuadrática introduce más curvatura que la lineal, pero la cúbica generalmente ofrece una mejor aproximación para fenómenos físicos continuos como la deflexión de una viga.\n")
    texto_resultados.insert(tk.END, "Para determinar el método *más* adecuado en un contexto real, se necesitaría información adicional sobre el comportamiento esperado de la viga (por ejemplo, de modelos teóricos) o más puntos de datos experimentales para validar las interpolaciones.\n")

# Crear un botón para mostrar los resultados
boton_mostrar = tk.Button(ventana, text="Mostrar Resultados", command=mostrar_resultados)
boton_mostrar.pack(pady=5)

# Graficar los resultados en una ventana separada de Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(longitud, deflexion, color='red', label='Datos Experimentales')
ax.plot(longitud_interp, deflexion_lineal, '--', color='blue', label='Interpolación Lineal')
ax.plot(longitud_interp, deflexion_cuadratica, '-.', color='green', label='Interpolación Cuadrática')
ax.plot(longitud_interp, deflexion_cubica, color='purple', label='Interpolación Cúbica')
ax.set_xlabel('Longitud (m)')
ax.set_ylabel('Deflexión (mm)')
ax.set_title('Análisis de Deflexión de Viga mediante Interpolación')
ax.legend()
ax.grid(True)

# Mostrar la gráfica de Matplotlib dentro de la ventana de Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10)

toolbar = NavigationToolbar2Tk(canvas, ventana)
toolbar.update()
canvas_widget.pack()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()