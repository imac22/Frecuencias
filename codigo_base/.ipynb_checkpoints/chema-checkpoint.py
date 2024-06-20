def fa_grouped(numeros, lim_inf, lim_sup):

  # Inicializar la lista de frecuencias
  frecuencias = [0] * len(lim_inf)

  # Contar las frecuencias para cada clase
  for numero in numeros:
    # Recorrer las clases
    for i in range(len(lim_inf)):
        if lim_inf[i] <= numero <= lim_sup[i]:
            frecuencias[i] +=1
            break

  return frecuencias

