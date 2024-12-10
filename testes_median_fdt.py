from fdt_default import fdt_default
from median_fdt import median_fdt

# Dados de exemplo
dados = [10, 12, 15, 20, 22, 25, 25, 30, 35, 40]

# Criar uma tabela de frequências agrupada (fdt)
tabela_fdt = fdt_default(dados)

# Visualizar o resultado
print(tabela_fdt['table'])

# Calcular a mediana
mediana = median_fdt(tabela_fdt)
print("A mediana é:", mediana)