def plot_ojiva(clases, fr_acum, marcas_texto, labelx, labely, titulo):

    import matplotlib.pyplot as plt

    # Datos
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico

    # Ajustes para el graficado del polígono
    datos_x = [0] + clases 
    datos_y = [0] + fr_acum 


    plt.plot(datos_x, datos_y, 
            linewidth=5, color="g", linestyle="--", 
            marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(clases, marcas_texto, fontsize=15, rotation=0)
    plt.xlabel(labelx, fontsize=25)  # Etiqueta del eje x
    plt.ylabel(labely, fontsize=25)  # Etiqueta del eje y
    plt.title(titulo, fontsize=40)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico


