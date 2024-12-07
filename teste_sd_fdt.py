import numpy as np
from sd_fdt_default import sd_fdt

# Função para testar sd_fdt
def testar_sd_fdt():
    print("Testando sd_fdt...")

    # Teste 1: Caso básico
    x_test_1 = {
        'breaks': {'start': 0, 'end': 40, 'n': 4},
        'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])
    }
    resultado_1 = sd_fdt(x_test_1)
    esperado_1 = 9.8
    print(f"Teste 1 - Resultado obtido: {resultado_1}, Esperado: {esperado_1}")
    assert np.isclose(resultado_1, esperado_1, atol=0.01), "Erro no Teste 1: cálculo do desvio padrão"

    # Teste 2: Frequências mais altas
    x_test_2 = {
        'breaks': {'start': 0, 'end': 50, 'n': 5},
        'table': np.array([[1, 10], [2, 20], [3, 30], [4, 25], [5, 15]])
    }
    resultado_2 = sd_fdt(x_test_2)
    esperado_2 = 12.03  # Calculado previamente
    print(f"Teste 2 - Resultado obtido: {resultado_2}, Esperado: {esperado_2}")
    assert np.isclose(resultado_2, esperado_2, atol=0.01), "Erro no Teste 2: cálculo do desvio padrão"

    # Teste 3: Distribuição uniforme
    x_test_3 = {
        'breaks': {'start': 0, 'end': 100, 'n': 5},
        'table': np.array([[1, 20], [2, 20], [3, 20], [4, 20], [5, 20]])
    }
    resultado_3 = sd_fdt(x_test_3)
    esperado_3 = 28.72  # Calculado previamente
    print(f"Teste 3 - Resultado obtido: {resultado_3}, Esperado: {esperado_3}")
    assert np.isclose(resultado_3, esperado_3, atol=0.01), "Erro no Teste 3: cálculo do desvio padrão"

    # Teste 4: Frequência única (caso limite)
    x_test_4 = {
        'breaks': {'start': 0, 'end': 10, 'n': 1},
        'table': np.array([[1, 100]])
    }
    resultado_4 = sd_fdt(x_test_4)
    esperado_4 = 0.0  # Apenas um intervalo, sem desvio
    print(f"Teste 4 - Resultado obtido: {resultado_4}, Esperado: {esperado_4}")
    assert np.isclose(resultado_4, esperado_4, atol=0.01), "Erro no Teste 4: cálculo do desvio padrão"

if __name__ == "__main__":
    testar_sd_fdt()
