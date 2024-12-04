import numpy as np
from mean import mean_fdt
from var_fdt_default import var_fdt
from sd_fdt_default import sd_fdt

# Teste para a função mean_fdt
def testar_mean_fdt():
    print("Testando mean_fdt...")
    x_test = {
        'breaks': {'start': 0, 'end': 40, 'h': 10},
        'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])
    }
    resultado = mean_fdt(x_test)
    esperado = 22.5
    print(f"Resultado obtido: {resultado}")
    print(f"Esperado: {esperado}")
    assert np.isclose(resultado, esperado), "Erro no cálculo da média"

# Teste para a função var_fdt
def testar_var_fdt():
    print("Testando var_fdt...")
    x_test = {
        'breaks': {'start': 0, 'end': 40, 'h': 10},
        'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])
    }
    resultado = var_fdt(x_test)
    esperado = 96.15
    print(f"Resultado obtido: {resultado}")
    print(f"Esperado: {esperado}")
    assert np.isclose(resultado, esperado, atol=0.01), "Erro no cálculo da variância"

# Teste para a função sd_fdt
def testar_sd_fdt():
    print("Testando sd_fdt...")
    x_test = {
        'breaks': {'start': 0, 'end': 40, 'n': 4},
        'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])
    }
    resultado = sd_fdt(x_test)
    esperado = 9.8
    print(f"Resultado obtido: {resultado}")
    print(f"Esperado: {esperado}")
    assert np.isclose(resultado, esperado, atol=0.01), "Erro no cálculo do desvio padrão"

if __name__ == "__main__":
    # Executa todos os testes
    print("Executando todos os testes...\n")
    testar_mean_fdt()
    testar_var_fdt()
    testar_sd_fdt()
