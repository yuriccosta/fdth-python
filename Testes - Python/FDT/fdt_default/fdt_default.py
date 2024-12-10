import numpy as np  # Importa a biblioteca numpy para manipulação de arrays e cálculos matemáticos.
from make_fdt_simple import make_fdt_simple  # Importa a função make_fdt_simple, que provavelmente cria a tabela de distribuição de frequência.

def fdt_default(x, k=None, start=None, end=None, h=None, breaks='Sturges', right=False, na_rm=False):
    """
    Define a função fdt_default, que gera uma tabela de distribuição de frequência (FDT) com configurações padrão ou especificadas.

    Parâmetros:
    - x: Dados de entrada (array ou lista).
    - k: Número de classes (opcional).
    - start: Início do intervalo (opcional).
    - end: Fim do intervalo (opcional).
    - h: Largura das classes (opcional).
    - breaks: Método de cálculo do número de classes ('Sturges', 'Scott', 'FD'). Padrão: 'Sturges'.
    - right: Indica se os intervalos incluem o limite direito. Padrão: False.
    - na_rm: Remove valores ausentes (<NA>) se True. Padrão: False.

    Retorno:
    - Dicionário contendo a tabela de distribuição e detalhes dos intervalos.
    """
    x = np.array([np.nan if v is None else v for v in x], dtype=np.float64)
    # Converte os dados de entrada (x) em um array NumPy, substituindo valores None por NaN e garantindo que sejam floats.

    if not np.issubdtype(x.dtype, np.number):
        raise TypeError("The data vector must be numeric.")
        # Verifica se os dados são numéricos; caso contrário, gera um erro.

    if na_rm:
        x = x[~np.isnan(x)]
        # Se na_rm for True, remove os valores NaN do array.
    elif np.any(np.isnan(x)):
        raise ValueError("The data has <NA> values and na.rm=FALSE by default.")
        # Se houver NaN e na_rm for False, lança um erro informando que os dados contêm valores ausentes.

    # Determinação do número de classes e/ou largura dos intervalos com base nos parâmetros fornecidos.
    if k is None and start is None and end is None and h is None:
        # Se nenhum parâmetro específico foi fornecido, utiliza o método definido em 'breaks'.
        if breaks == 'Sturges':
            k = int(np.ceil(1 + 3.322 * np.log10(len(x))))
            # Método de Sturges: calcula o número de classes baseado no tamanho dos dados.
        elif breaks == 'Scott':
            std_dev = np.std(x)
            k = int(np.ceil((x.max() - x.min()) / (3.5 * std_dev / (len(x) ** (1 / 3)))))
            # Método de Scott: utiliza o desvio padrão para determinar a largura dos intervalos.
        elif breaks == 'FD':
            iqr = np.percentile(x, 75) - np.percentile(x, 25)
            k = int(np.ceil((x.max() - x.min()) / (2 * iqr / (len(x) ** (1 / 3)))))
            # Método de Freedman-Diaconis (FD): baseado no intervalo interquartil (IQR).
        else:
            raise ValueError("Invalid 'breaks' method.")
            # Se o método fornecido for inválido, lança um erro.

        start, end = x.min() - abs(x.min()) / 100, x.max() + abs(x.max()) / 100
        # Define os limites inferior e superior com um pequeno ajuste para evitar exclusão de valores extremos.
        R = end - start  # Calcula o intervalo total dos dados.
        h = R / k  # Determina a largura de cada classe.

    elif start is None and end is None and h is None:
        # Se apenas k foi fornecido, calcula start, end e h com base no número de classes.
        start, end = x.min() - abs(x.min()) / 100, x.max() + abs(x.max()) / 100
        R = end - start
        h = R / k

    elif k is None and h is None:
        # Se start e end são fornecidos, calcula k e h com base no intervalo total.
        R = end - start
        k = int(np.sqrt(abs(R)))  # Usa a raiz quadrada do intervalo total como estimativa inicial.
        k = max(k, 5)  # Garante que o número mínimo de classes seja 5.
        h = R / k  # Calcula a largura das classes.

    elif k is None:
        pass  # Caso h seja fornecido, ignora o cálculo de k.

    else:
        raise ValueError("Please check the function syntax!")
        # Lança um erro se os parâmetros fornecidos forem conflitantes ou inválidos.

    # Geração da tabela de distribuição de frequência
    table = make_fdt_simple(x, start, end, h, right)
    # Chama a função make_fdt_simple para criar a tabela com os parâmetros calculados.
    
    breaks_info = {'start': start, 'end': end, 'h': h, 'right': int(right)}
    # Armazena os detalhes dos intervalos em um dicionário.

    result = {'table': table, 'breaks': breaks_info}
    # Combina a tabela de distribuição e os detalhes dos intervalos em um único dicionário.

    return result
    # Retorna o resultado final contendo a tabela e os parâmetros de binagem.
