def fa_grouped(datos, lim_inf, lim_sup):

    fr = [0] * len(lim_inf)
    
    clases = [0] * len(lim_inf)  
    for i in range(len(lim_inf)):
        clases[i] = i + 1 
    for elemento in datos:
    
        for i in range(len(lim_inf)):
            if lim_inf[i] <= elemento <= lim_sup[i]:
                fr[i] +=1
            break

    return fr, clases

