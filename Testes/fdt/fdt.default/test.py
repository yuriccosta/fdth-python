import numpy as np
from fdt_default import fdt_default

"""
#Test 1
dados = np.array([2, 5, 7, 10, 12, 15, 18])
resultado = fdt_default(dados, breaks='FD')
print(resultado['table'])


#Test 2
dados = np.array([3, 6, 9, 12, 15, 18, 21])
resultado = fdt_default(dados, k=4)
print(resultado['table'])


#Test 3
dados = np.array([1, 4, 7, 10, 13, 16, 19])
resultado = fdt_default(dados, start=0, end=20)
print(resultado['table'])

#Test 4
dados = np.array([10, 15, 20, 25, 30, 35, 40])
resultado = fdt_default(dados, start=10, end=50, h=8)
print(resultado['table'])

#Test 5
try:
    dados = np.array([2, None, 8, 10, None, 18])
    resultado = fdt_default(dados, na_rm=False)
except ValueError as e:
    print("Erro:", e)

#Test 6
try:
    dados = np.array([1, 2, 3, 4])
    resultado = fdt_default(dados, start=1, end=5, k=2, h=1)
except ValueError as e:
    print("Erro:", e)
"""
#Test 4
dados = np.array([10, 15, 20, 25, 30, 35, 40])
resultado = fdt_default(dados, start=10, end=50, h=8)
print(resultado['table'])