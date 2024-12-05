import numpy as np
from sd_fdt_default import sd_fdt

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
    testar_sd_fdt()
