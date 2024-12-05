import numpy as np
from var_fdt_default import var_fdt

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

if __name__ == "__main__":
    testar_var_fdt()
