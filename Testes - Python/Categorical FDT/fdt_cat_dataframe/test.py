import pandas as pd
from fdt_cat_data_frame import fdt_cat_data_frame  # Ensure the function and class are in the same directory


# Test 1: Sem agrupamento
# Verifica a geração de tabelas de frequência para um DataFrame com colunas categóricas,
# sem considerar agrupamento. Ordena os resultados de forma decrescente.

df1 = pd.DataFrame({
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y'])
})
result1 = fdt_cat_data_frame(df1, sort=True, decreasing=True)
print(result1)

"""
# Test 2: Com agrupamento
# Avalia a funcionalidade da função ao agrupar os dados por uma coluna específica ("group"),
# criando tabelas de frequência para as colunas categóricas dentro de cada grupo.
# Ordena os resultados de forma crescente.

df2 = pd.DataFrame({
    'group': pd.Categorical(['G1', 'G1', 'G2', 'G2', 'G2']),
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y'])
})
result2 = fdt_cat_data_frame(df2, by='group', sort=True, decreasing=False)
print(result2)

# Test 3: Com coluna numérica
# Testa a função em um DataFrame que contém colunas categóricas e uma coluna numérica.
# Gera tabelas de frequência apenas para as colunas categóricas, ignorando a coluna numérica.
# Não realiza ordenação nas tabelas.

df3 = pd.DataFrame({
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y']),
    'col3': [1, 2, 3, 4, 5]  # Numeric column
})
result3 = fdt_cat_data_frame(df3, sort=False)
print(result3)
"""

