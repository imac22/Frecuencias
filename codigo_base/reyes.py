def plot_pie(frecuencias, marcas_texto):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 8))
    plt.pie(frecuencias,
            autopct="%0.1f%%",
            colors=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"],
            labels=marcas_texto)
    plt.title("Gráfico de Pastel", fontsize=20)
    plt.show()

    return frecuencias 
