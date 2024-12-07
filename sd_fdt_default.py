import numpy as np
from mean import mean_fdt  # Importando a função mean_fdt


def sd_fdt(x):
    """
    Calcula o desvio padrão ponderado para uma tabela de frequência.

    Parâmetros:
    x (dict): Dicionário contendo as informações:
        - 'breaks': Dicionário com 'start', 'end' e 'n' para definir os intervalos.
        - 'table': Array NumPy contendo as frequências.

    Retorna:
    float: O desvio padrão ponderado.
    """
    # Validação da estrutura de entrada
    required_keys = ['breaks', 'table']
    for key in required_keys:
        if key not in x:
            raise KeyError(f"A chave '{key}' está ausente em 'x'.")
    if not all(k in x['breaks'] for k in ['start', 'end', 'n']):
        raise KeyError("As chaves 'start', 'end' e 'n' devem estar presentes em 'x['breaks']'.")

    # Definir intervalos de classe com base nos valores 'start', 'end' e 'n'
    breaks = np.linspace(x['breaks']['start'], x['breaks']['end'], x['breaks']['n'] + 1)

    # Calcular pontos médios dos intervalos de classe
    mids = 0.5 * (breaks[:-1] + breaks[1:])

    # Frequências das classes
    y = x['table'][:, 1]

    # Calcular média usando a função mean_fdt
    mean_fdt_value = mean_fdt(x)

    # Calcular variância ponderada
    res = np.sum((mids - mean_fdt_value) ** 2 * y) / (np.sum(y) - 1)

    # Retornar o desvio padrão
    return np.sqrt(res)
