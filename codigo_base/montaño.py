def plot_poligono(marcas_clase, frecuencias, marcas_texto):
    import matplotlib.pyplot as plt

# Datos
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico


    # Ajustes para el graficado del polígono
    datos_x = [0] + marcas_clase + [7]
    datos_y = [0] + frecuencias + [0]

    plt.plot(datos_x, datos_y, 
        linewidth=5, color="g", linestyle="--", 
        marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(marcas_clase, marcas_texto, fontsize=12, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=15)  # Etiqueta del eje x
    plt.ylabel("Frecuencia", fontsize=15)  # Etiqueta del eje y
    plt.title("Polígono de frecuencias", fontsize=20)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico
    return marcas_clase, frecuencias, marcas_texto