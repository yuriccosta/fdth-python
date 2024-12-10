from mfv_default import mfv_default

# Conjunto de dados com uma única moda
data1 = [1, 2, 2, 3, 4]
print("A moda de data1 é:", mfv_default(data1))

# Conjunto de dados com múltiplas modas
data2 = [1, 1, 2, 2, 3]
print("A moda de data2 é:", mfv_default(data2))

# Conjunto de dados onde todos os valores são únicos
data3 = [1, 2, 3, 4, 5]
print("A moda de data3 é:", mfv_default(data3))

# Conjunto de dados onde todos os valores são iguais
data4 = [2, 2, 2, 2, 2]
print("A moda de data4 é:", mfv_default(data4))

# Conjunto de dados vazio
data5 = []
print("A moda de data5 é:", mfv_default(data5))

# Conjunto de dados com valores não numéricos
data6 = ['a', 'b', 'b', 'c']
print("A moda de data6 é:", mfv_default(data6))