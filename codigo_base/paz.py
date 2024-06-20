def plot_barras(marcas_clase, frecuencias, marcas_texto):
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico

        # marcas_clase = [0.165, 0.495, 0.825, 1.155, 1.485]  # Datos del eje x
        # frecuencias = [6, 4, 3, 3, 4]  # Datos del eje y
        # marcas_texto = ["0.165", "0.495", "0.825", "1.155", "1.485"]

        plt.barh(marcas_clase, frecuencias,
                height=0.5, edgecolor="k",
                color=["#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#333CFF", "#33FFBE"])

        plt.yticks(marcas_clase, marcas_texto, fontsize=12, rotation=45)
        plt.xlabel("Frecuencia absoluta", fontsize=15)  # Etiqueta del eje x
        plt.ylabel("Marcas de clase", fontsize=15)  # Etiqueta del eje y
        plt.title("Diagrama de barras", fontsize=20)  # Etiqueta del título
        plt.grid()  # Activar cuadrícula
        plt.show()  # Mostrar gráfico

        return marcas_clase, frecuencias, marcas_texto