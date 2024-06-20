 import pandas as pd
def tabla_grouped(lim_inf, lim_sup, mrks, fa, fr, facum):
   
    # Create the DataFrame with column headers
    data = {'Clases': clases_sorted,
            'Limite inferior': lim_inf,
            'Limite inferior': lim_sup,
            'Marcas de clase': mrks,
            'Frecuencia absoluta': fa,
            'Frecuencia Relativa': fr,
            'Frecuencia Acumulada': facum}
    
    df = pd.DataFrame(data)
    return df
    