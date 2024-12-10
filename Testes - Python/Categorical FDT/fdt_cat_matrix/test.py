from fdt_cat_matrix import fdt_cat_matrix
import numpy as np
import pandas as pd
"""
# Test 1: Verifica a criação de tabelas de distribuição de frequência
# para uma matriz de categorias distintas distribuídas igualmente
# em várias colunas. Ordena os resultados em ordem decrescente.

x = np.array([
    ["A", "B", "C"],
    ["A", "B", "C"],
    ["B", "A", "C"],
    ["C", "A", "B"]
])
df = pd.DataFrame(x, columns=["Col1", "Col2", "Col3"])
res = fdt_cat_matrix(df, sort=True, decreasing=True)
print(res)

# Test 2: Testa a criação de tabelas de distribuição de frequência
# para uma matriz com valores homogêneos (mesmas categorias em todas
# as colunas e linhas). Ordena os resultados em ordem decrescente.

x = np.array([
    ["X", "Y", "Z"],
    ["X", "Y", "Z"],
    ["X", "Y", "Z"],
    ["X", "Y", "Z"]
])
df = pd.DataFrame(x, columns=["Col1", "Col2", "Col3"])
res = fdt_cat_matrix(df, sort=True, decreasing=True)
print(res)
"""
# Test 3: Avalia a criação de tabelas de frequência para uma matriz
# com categorias variadas em cada coluna. Ordena os resultados em
# ordem crescente.

x = np.array([
    ["Dog", "Cat", "Fish"],
    ["Dog", "Dog", "Bird"],
    ["Cat", "Cat", "Fish"],
    ["Fish", "Dog", "Bird"]
])
df = pd.DataFrame(x, columns=["Col1", "Col2", "Col3"])
res = fdt_cat_matrix(df, sort=True, decreasing=False)
print(res)

