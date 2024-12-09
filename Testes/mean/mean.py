import numpy as np

def mean_fdt(x):
    # Definir intervalos de classe com base nos valores 'start', 'end' e 'h'
    breaks = np.arange(x['breaks']['start'], x['breaks']['end'] + x['breaks']['h'], x['breaks']['h'])
    
    # Calcular pontos médios dos intervalos de classe
    mids = 0.5 * (breaks[:-1] + breaks[1:])
    
    # Frequências das classes
    y = x['table'][:, 1]
    
    # Calcular a média ponderada dos pontos médios
    res = np.sum(y * mids) / np.sum(y)
    
    # Retornar a média
    return res


