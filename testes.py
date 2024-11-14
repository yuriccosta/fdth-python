from summary_fdt_default import summary_fdt_default
import pandas as pd


# Definindo o objeto de teste
object1 = {
    'table': pd.DataFrame({
        'Class limits': ['(1, 2)', '(3, 4)', '[5, 6]'],
        'f': [10, 20, 30],
        'rf': [0.1, 0.2, 0.3],
        'rf(%)': [10, 20, 30],
        'cf': [10, 30, 60],
        'cf(%)': [10, 30, 60]
    }),
    'breaks': {'right': [True, True, True]}
}

# Chamando a função para exibir o resumo
print("Teste 1: Teste Simples com Frequências Inteiras")
summary_fdt_default(object1, format_classes=False, columns=range(6), round=2)
print()

# Definindo o objeto de teste
object2 = {
    'table': pd.DataFrame({
        'Class limits': ['(1, 2)', '(3, 4)', '[5, 6]'],
        'f': [10, 20, 30],
        'rf': [0.1, 0.2, 0.3],
        'rf(%)': [10, 20, 30],
        'cf': [10, 30, 60],
        'cf(%)': [10, 30, 60]
    }),
    'breaks': {'right': [True, True, True]}
}

# Chamando a função para exibir o resumo com formatação de classes
print("Teste 2: Teste com Formatação de Classes")
summary_fdt_default(object2, format_classes=True, columns=range(6), round=2)
print()

# Definindo o objeto de teste
object3 = {
    'table': pd.DataFrame({
        'Class limits': ['(1, 2)', '(3, 4)', '[5, 6]'],
        'f': [10, 20, 30],
        'rf': [0.1, 0.2, 0.3],
        'rf(%)': [10, 20, 30],
        'cf': [10, 30, 60],
        'cf(%)': [10, 30, 60]
    }),
    'breaks': {'right': [True, True, True]}
}

# Chamando a função para exibir apenas as três primeiras colunas
print("Teste 3: Teste com Colunas Selecionadas")
summary_fdt_default(object3, format_classes=False, columns=range(3), round=2)
print()

# Definindo o objeto de teste
object4 = {
    'table': pd.DataFrame({
        'Class limits': ['(1, 2)', '(3, 4)', '[5, 6]'],
        'f': [10.567, 20.234, 30.876],
        'rf': [0.105, 0.205, 0.305],
        'rf(%)': [10.5, 20.5, 30.5],
        'cf': [10, 30, 60],
        'cf(%)': [10.0, 30.0, 60.0]
    }),
    'breaks': {'right': [True, True, True]}
}

# Chamando a função para exibir o resumo com arredondamento para 1 casa decimal
print("Teste 4: Teste com Arredondamento de Valores")
summary_fdt_default(object4, format_classes=False, columns=range(6), round=1)
print()

# Definindo o objeto de teste
object5 = {
    'table': pd.DataFrame({
        'Class limits': ['(1, 2)', '(3, 4)', '[5, 6]'],
        'f': [12, 15, 8],
        'rf': [0.24, 0.30, 0.16],
        'rf(%)': [24.0, 30.0, 16.0],
        'cf': [12, 27, 35],
        'cf(%)': [24.0, 54.0, 70.0]
    }),
    'breaks': {'right': [True, True, True]}
}

# Chamando a função para exibir o resumo
print("Teste 5: Teste com Variação nas Frequências")
summary_fdt_default(object5, format_classes=False, columns=range(6), round=2)
print()

# Definindo o objeto para o teste 6 em Python
object6 = {
    'table': pd.DataFrame({
        'Class limits': ['(1, 2)', '(3, 4)', '[5, 6]'],
        'f': [12, 15, 8],
        'rf': [0.24, 0.30, 0.16],
        'rf(%)': [24.0, 30.0, 16.0],
        'cf': [12, 27, 35],
        'cf(%)': [24.0, 54.0, 70.0]
    }),
    'breaks': {'right': [True, True, True]}
}

# Chamando a função em Python com padrão simples
print("Teste 6: Teste com Padrão Simples de Formatação (pattern)")
summary_fdt_default(object6, format_classes=True, columns=range(6), round=2, pattern='{0:09.2f}')
print()