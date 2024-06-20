def plot_ojiva(marcas_clase, fa_acumulada, marcas_texto):

    import matplotlib.pyplot as plt

    # Datos
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico

    # marcas_clase = [0.165, 0.495, 0.825, 1.155, 1.485]  # Datos del eje x
    # frecuencias = [6, 10, 13, 16, 20]  # Datos del eje y
    # marcas_texto = ["0.165", "0.495", "0.825", "1.155", "1.485"]

    # Ajustes para el graficado del polígono
    datos_x = [0] + marcas_clase 
    datos_y = [0] + fa_acumulada 

    # El Polígono de frecuencias tiene:
    # - Forma del marcador triangular (Marker = "v")
    # - Una línea con estilo "cortadita" o discontinua.

    plt.plot(datos_x, datos_y, 
            linewidth=5, color="g", linestyle="--", 
            marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=0)
    plt.xlabel("Marcas de clase", fontsize=25)  # Etiqueta del eje x
    plt.ylabel("Frecuencia acumulada", fontsize=25)  # Etiqueta del eje y
    plt.title("Ojiva", fontsize=40)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico

    return marcas_clase, fa_acumulada, marcas_texto