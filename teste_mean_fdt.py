import numpy as np
from mean import mean_fdt

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

if __name__ == "__main__":
    testar_mean_fdt()
