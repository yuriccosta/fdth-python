import numpy as np
from mean import mean_fdt  # Certifique-se de que a função mean_fdt está no arquivo mean.py

# Função sd_fdt
def sd_fdt(x):
    # Definir intervalos de classe com base nos valores 'start', 'end' e 'h'
    breaks = np.arange(x['breaks']['start'], x['breaks']['end'] + x['breaks']['h'], x['breaks']['h'])
    
    # Calcular pontos médios dos intervalos de classe
    mids = 0.5 * (breaks[:-1] + breaks[1:])
    
    # Frequências das classes
    y = x['table'][:, 1]
    
    # Calcular média usando a função mean_fdt
    mean_fdt_value = mean_fdt(x)
    
    # Calcular variância ponderada
    res = np.sum((mids - mean_fdt_value) ** 2 * y) / (np.sum(y) - 1)
    
    # Retornar o desvio padrão
    return np.sqrt(res)
