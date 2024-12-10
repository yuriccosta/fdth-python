import numpy as np
import pandas as pd

def median_fdt(data):
    # Extrai a tabela de frequência do objeto data
    fdt = data['table']
    
    # Número total de observações
    n = fdt.iloc[-1, 4]
    
    # Posição da classe mediana
    posM = (n / 2 <= fdt.iloc[:, 4]).idxmax()
    
    # Intervalos de classe
    breaks = data['breaks']
    brk = np.arange(breaks['start'], breaks['end'] + breaks['h'], breaks['h'])
    
    # Limite inferior da classe mediana
    liM = brk[posM]
    
    # Frequência acumulada anterior à classe mediana
    if posM - 1 < 0:
        sfaM = 0
    else:
        sfaM = fdt.iloc[posM - 1, 4]
    
    # Frequência da classe mediana
    fM = fdt.iloc[posM, 1]
    
    # Largura da classe
    h = breaks['h']
    
    # Cálculo da mediana
    res = liM + (((n / 2) - sfaM) * h) / fM
    
    return res
