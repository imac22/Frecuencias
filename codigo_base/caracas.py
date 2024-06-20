def plot_hist(marcas_clase, frecuencias, marcas_texto):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))  # Set the figure size

    plt.bar(marcas_clase, frecuencias,
           width=0.3, edgecolor="k",
           color=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"])
    
    plt.xticks(marcas_clase, marcas_texto, fontsize=12)
    plt.xlabel("Marcas de clase", fontsize=15)  # X-axis label
    plt.ylabel("Frecuencia absoluta", fontsize=15)  # Y-axis label
    plt.title("Histograma", fontsize=20)  # Title
    plt.grid()  # Enable grid
    plt.show()  # Display the plot
    
    return marcas_clase, frecuencias, marcas_texto