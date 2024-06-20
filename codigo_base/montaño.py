def plot_poligono(clases, fa_sorted,marcas_texto):
    import matplotlib.pyplot as plt

# Datos
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico


    # Ajustes para el graficado del polígono
    datos_x = [0] + clases + [7]
    datos_y = [0] + fa_sorted + [0]

    plt.plot(datos_x, datos_y, 
        linewidth=5, color="g", linestyle="--", 
        marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(clases, marcas_texto, fontsize=12, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=15)  # Etiqueta del eje x
    plt.ylabel("Frecuencia", fontsize=15)  # Etiqueta del eje y
    plt.title("Polígono de frecuencias", fontsize=20)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico
    return clases, fa_sorted, marcas_texto