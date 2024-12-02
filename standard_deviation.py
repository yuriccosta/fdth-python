import numpy as np

def sd_fdt(x):
    # Definir intervalos de classe com base nos valores 'start', 'end' e 'n'
    breaks = np.linspace(x['breaks']['start'], x['breaks']['end'], x['breaks']['n'] + 1)
    
    # Calcular pontos médios dos intervalos de classe
    mids = 0.5 * (breaks[:-1] + breaks[1:])
    
    # Frequências das classes
    y = x['table'][:, 1]
    
    # Calcular média ponderada dos pontos médios
    mean_fdt = np.average(mids, weights=y)
    
    # Calcular variância ponderada
    res = np.sum((mids - mean_fdt) ** 2 * y) / (np.sum(y) - 1)
    
    # Retornar o desvio padrão
    return np.sqrt(res)

'''
# Exemplo de entrada de teste
x_test = {
    'breaks': {'start': 0, 'end': 40, 'n': 4},  # Define 4 intervalos de 0 a 40
    'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])  # Frequências para cada classe
}

# Executar a função e imprimir o resultado
resultado = sd_fdt(x_test)
print("Desvio Padrão:", resultado)

'''