import numpy as np  # Importa a biblioteca numpy para manipulação de arrays e cálculos numéricos.
import pandas as pd  # Importa a biblioteca pandas para manipulação de tabelas e DataFrames.
from make_fdt_multiple import make_fdt_multiple  # Importa a função que cria tabelas de distribuição de frequência para múltiplas colunas.

class FDTMatrixResult:
    """
    Classe para encapsular os resultados de tabelas de distribuição de frequência para matrizes
    e fornecer saída formatada.
    """
    def __init__(self, results):
        self.results = results  # Armazena os resultados das tabelas de distribuição.

    def __str__(self):
        # Define a representação em string para a classe, formatando os resultados de forma amigável.
        output = []  # Lista para armazenar as strings de saída.
        for key, value in self.results.items():
            # Itera pelos resultados, onde key é o nome da coluna e value contém a tabela e os intervalos.
            output.append(f"--- {key} ---")  # Adiciona o cabeçalho com o nome da coluna.
            
            # Formata a tabela adicionando números de linha começando de 1.
            table = value["table"]
            table.index = range(1, len(table) + 1)  # Define os índices da tabela a partir de 1.
            output.append("Table:")  # Adiciona um rótulo para a tabela.
            output.append(table.to_string(index=True, header=True))  # Adiciona a tabela com cabeçalhos e índices.
            
            # Formata os intervalos (breaks) como uma tabela simplificada.
            breaks_df = pd.DataFrame([value["breaks"].values()],
                                     columns=value["breaks"].keys())
            # Cria um DataFrame para formatar os valores dos intervalos.
            output.append("\nBreaks:")  # Adiciona um rótulo para os intervalos.
            output.append(breaks_df.to_string(index=False, header=True))  # Adiciona os intervalos formatados.
            output.append("")  # Linha vazia para separar as seções.

        return "\n".join(output)  # Junta todas as strings formatadas em uma única saída.

def fdt_matrix(x, k=None, breaks="Sturges", right=False, na_rm=False):
    """
    Gera tabelas de distribuição de frequência para cada coluna de uma matriz.

    Parâmetros:
    - x: Matriz de entrada (numpy.ndarray) com dados numéricos.
    - k: Número de classes para o histograma. Padrão: None.
    - breaks: Método para calcular o número de classes ('Sturges', 'Scott', 'FD').
    - right: Indica se os intervalos incluem o limite direito. Padrão: False.
    - na_rm: Remove valores ausentes (<NA>) se True. Padrão: False.

    Retorno:
    - FDTMatrixResult: Objeto personalizado contendo as tabelas de distribuição de frequência.
    """
    if not isinstance(x, np.ndarray):
        raise ValueError("Input x must be a numpy.ndarray.")
        # Verifica se a entrada x é um array NumPy. Caso contrário, lança um erro.

    results = {}  # Dicionário para armazenar os resultados das tabelas por coluna.

    # Itera por cada coluna da matriz.
    for i in range(x.shape[1]):
        col_data = x[:, i]
        # Seleciona os dados da coluna i (todas as linhas e apenas a coluna i).

        # Chama a função make_fdt_multiple para processar a coluna.
        fdt_result = make_fdt_multiple(col_data, k=k, breaks=breaks, right=right, na_rm=na_rm)
        
        # Armazena os resultados em um dicionário.
        col_name = f"Column:{i+1}"  # Nomeia a coluna (começando de 1).
        results[col_name] = {
            "table": fdt_result["table"],  # Armazena a tabela (assumindo que seja um DataFrame do pandas).
            "breaks": fdt_result["breaks"]  # Armazena os intervalos (um dicionário).
        }

    return FDTMatrixResult(results)
    # Retorna um objeto FDTMatrixResult contendo todas as tabelas e intervalos formatados.
