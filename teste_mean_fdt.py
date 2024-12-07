import numpy as np
from mean import mean_fdt

# Teste para a função mean_fdt
def testar_mean_fdt():
    print("Testando mean_fdt...")

    # Teste 1 - Caso base
    x_test1 = {
        'breaks': {'start': 0, 'end': 40, 'h': 10},
        'table': np.array([[1, 5], [2, 10], [3, 15], [4, 10]])
    }
    resultado1 = mean_fdt(x_test1)
    esperado1 = 22.5
    print(f"Resultado obtido: {resultado1}")
    print(f"Esperado: {esperado1}")
    assert np.isclose(resultado1, esperado1), "Erro no cálculo da média - Teste 1"

    # Teste 2 - Intervalos menores e distribuição uniforme
    x_test2 = {
        'breaks': {'start': 0, 'end': 20, 'h': 5},
        'table': np.array([[1, 10], [2, 10], [3, 10], [4, 10]])
    }
    resultado2 = mean_fdt(x_test2)
    esperado2 = 10.0  # Valor fictício, substituir pelo correto
    print(f"Resultado obtido: {resultado2}")
    print(f"Esperado: {esperado2}")
    assert np.isclose(resultado2, esperado2), "Erro no cálculo da média - Teste 2"

    # Teste 3 - Intervalos maiores e pesos variados
    x_test3 = {
        'breaks': {'start': 0, 'end': 100, 'h': 20},
        'table': np.array([[1, 5], [2, 15], [3, 10], [4, 20], [5, 10]])
    }
    resultado3 = mean_fdt(x_test3)
    esperado3 = 50.0  # Valor fictício, substituir pelo correto
    print(f"Resultado obtido: {resultado3}")
    print(f"Esperado: {esperado3}")
    assert np.isclose(resultado3, esperado3), "Erro no cálculo da média - Teste 3"

    # Teste 4 - Tabela com valores decrescentes
    x_test4 = {
        'breaks': {'start': 0, 'end': 50, 'h': 10},
        'table': np.array([[1, 20], [2, 15], [3, 10], [4, 5]])
    }
    resultado4 = mean_fdt(x_test4)
    esperado4 = 17.5  # Valor fictício, substituir pelo correto
    print(f"Resultado obtido: {resultado4}")
    print(f"Esperado: {esperado4}")
    assert np.isclose(resultado4, esperado4), "Erro no cálculo da média - Teste 4"

if __name__ == "__main__":
    testar_mean_fdt()
