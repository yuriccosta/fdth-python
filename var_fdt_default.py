import numpy as np
from var_fdt_default import var_fdt

# Teste para a função var_fdt
def testar_var_fdt():
    print("Testando var_fdt...")

    # Teste 1 - Caso base
    x_test1 = {
        'breaks': {'start': 0, 'end': 40, 'h': 10},
        'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])
    }
    resultado1 = var_fdt(x_test1)
    esperado1 = 96.15
    print(f"Resultado obtido: {resultado1}")
    print(f"Esperado: {esperado1}")
    assert np.isclose(resultado1, esperado1, atol=0.01), "Erro no cálculo da variância - Teste 1"

    # Teste 2 - Menor tabela e intervalo diferente
    x_test2 = {
        'breaks': {'start': 0, 'end': 20, 'h': 5},
        'table': np.array([[1, 8], [2, 12], [3, 10], [4, 5]])
    }
    resultado2 = var_fdt(x_test2)
    esperado2 = 66.67  # Valor fictício, substituir pelo correto
    print(f"Resultado obtido: {resultado2}")
    print(f"Esperado: {esperado2}")
    assert np.isclose(resultado2, esperado2, atol=0.01), "Erro no cálculo da variância - Teste 2"

    # Teste 3 - Tabela com valores uniformes
    x_test3 = {
        'breaks': {'start': 10, 'end': 50, 'h': 10},
        'table': np.array([[1, 10], [2, 10], [3, 10], [4, 10]])
    }
    resultado3 = var_fdt(x_test3)
    esperado3 = 0.0  # Variância de dados uniformes é zero
    print(f"Resultado obtido: {resultado3}")
    print(f"Esperado: {esperado3}")
    assert np.isclose(resultado3, esperado3, atol=0.01), "Erro no cálculo da variância - Teste 3"

    # Teste 4 - Tabela com valores maiores
    x_test4 = {
        'breaks': {'start': 0, 'end': 100, 'h': 20},
        'table': np.array([[1, 20], [2, 30], [3, 25], [4, 25]])
    }
    resultado4 = var_fdt(x_test4)
    esperado4 = 225.0  # Valor fictício, substituir pelo correto
    print(f"Resultado obtido: {resultado4}")
    print(f"Esperado: {esperado4}")
    assert np.isclose(resultado4, esperado4, atol=0.01), "Erro no cálculo da variância - Teste 4"

if __name__ == "__main__":
    testar_var_fdt()
