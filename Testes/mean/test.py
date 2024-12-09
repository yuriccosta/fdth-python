import numpy as np
from mean import mean_fdt

# Dados para os 4 testes
data_test1 = {
    'breaks': {'start': 0, 'end': 10, 'h': 2},
    'table': np.array([
        [0, 2],
        [2, 2],
        [4, 2],
        [6, 2],
        [8, 2]
    ])
}

data_test2 = {
    'breaks': {'start': 0, 'end': 12, 'h': 3},
    'table': np.array([
        [0, 1],
        [3, 2],
        [6, 3],
        [9, 4]
    ])
}

data_test3 = {
    'breaks': {'start': 0, 'end': 16, 'h': 4},
    'table': np.array([
        [0, 8],
        [4, 6],
        [8, 4],
        [12, 2]
    ])
}

data_test4 = {
    'breaks': {'start': 0, 'end': 20, 'h': 5},
    'table': np.array([
        [0, 3],
        [5, 7],
        [10, 5],
        [15, 2]
    ])
}

# Executando os testes
print("Teste 1:", mean_fdt(data_test1))
print("Teste 2:", mean_fdt(data_test2))
print("Teste 3:", mean_fdt(data_test3))
print("Teste 4:", mean_fdt(data_test4))