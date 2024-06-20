def obtener_fa(fr):
    frecuencias_acumuladas = []
    suma = 0
    for elemento in fr:
        suma += elemento
        frecuencias_acumuladas.append(suma)
    return frecuencias_acumuladas