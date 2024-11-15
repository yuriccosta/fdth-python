import numpy as np

def var_fdt(x):
    # Definir intervalos de classe com base nos valores 'start', 'end' e 'h'
    breaks = np.arange(x['breaks']['start'], x['breaks']['end'] + x['breaks']['h'], x['breaks']['h'])
    
    # Calcular pontos médios dos intervalos de classe
    mids = 0.5 * (breaks[:-1] + breaks[1:])
    
    # Frequências das classes
    y = x['table'][:, 1]
    
    # Calcular média ponderada dos pontos médios
    mean_fdt = np.average(mids, weights=y)
    
    # Calcular variância ponderada
    res = np.sum((mids - mean_fdt) ** 2 * y) / (np.sum(y) - 1)
    
    # Retornar a variância
    return res

'''
# Exemplo de entrada de teste para var_fdt
x_test = {
    'breaks': {
        'start': 0,  # Início do intervalo
        'end': 40,   # Final do intervalo
        'h': 10      # Incremento para cada intervalo (10 em 10)
    },
    'table': np.array([
        [1, 5],   # Intervalo 1, frequência 5
        [2, 10],  # Intervalo 2, frequência 10
        [3, 15],  # Intervalo 3, frequência 15
        [4, 10]   # Intervalo 4, frequência 10
    ])
}

#96.15
'''