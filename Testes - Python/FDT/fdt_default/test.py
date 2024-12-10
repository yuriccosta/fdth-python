import numpy as np
from fdt_default import fdt_default

"""
# Teste 1
# Testa o método de cálculo de classes usando a regra de Freedman-Diaconis ('FD').
dados = np.array([2, 5, 7, 10, 12, 15, 18])
resultado = fdt_default(dados, breaks='FD')
print(resultado['table'])

# Teste 2
# Testa a criação de uma tabela de frequência definindo um número fixo de classes (k=4).
dados = np.array([3, 6, 9, 12, 15, 18, 21])
resultado = fdt_default(dados, k=4)
print(resultado['table'])

# Teste 3
# Testa o uso de valores iniciais (start) e finais (end) personalizados para a tabela.
dados = np.array([1, 4, 7, 10, 13, 16, 19])
resultado = fdt_default(dados, start=0, end=20)
print(resultado['table'])

# Teste 4
# Testa a especificação de um intervalo fixo (h=8) para as classes, com limites iniciais e finais definidos.
dados = np.array([10, 15, 20, 25, 30, 35, 40])
resultado = fdt_default(dados, start=10, end=50, h=8)
print(resultado['table'])

# Teste 5
# Testa o comportamento da função ao encontrar valores ausentes (None) no array, com na_rm=False.
try:
    dados = np.array([2, None, 8, 10, None, 18])
    resultado = fdt_default(dados, na_rm=False)
except ValueError as e:
    print("Erro:", e)

# Teste 6
# Testa se a função detecta inconsistências nos parâmetros (k e h definidos simultaneamente).
try:
    dados = np.array([1, 2, 3, 4])
    resultado = fdt_default(dados, start=1, end=5, k=2, h=1)
except ValueError as e:
    print("Erro:", e)
"""

# Teste 1
# Testa o método de cálculo de classes usando a regra de Freedman-Diaconis ('FD').
dados = np.array([2, 5, 7, 10, 12, 15, 18])
resultado = fdt_default(dados, breaks='Sturges')
print(resultado['table'])
