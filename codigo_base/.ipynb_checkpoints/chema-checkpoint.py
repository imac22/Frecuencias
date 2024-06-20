import math
def fa_grouped(lim_inf, lim_sup, datos):
    freq_absoluta = []
    nclases = int(1 + (3.3*math.log10(len(datos))))
    for dato in datos:
        for i in range(nclases):
            if lim_inf <= dato < lim_sup:
                freq_absoluta[i] += 1
                break

    return freq_absoluta