import pandas as pd  # Importa a biblioteca pandas para manipulação de tabelas e DataFrames.
import numpy as np  # Importa a biblioteca numpy para manipulação de arrays e cálculos numéricos.
from make_fdt_multiple import make_fdt_multiple  
# Importa a função `make_fdt_multiple`, que gera tabelas de distribuição de frequência para colunas individuais.

class FDTResult:
    """
    Classe para encapsular os resultados das tabelas de distribuição de frequência
    e fornecer uma saída formatada.
    """
    def __init__(self, results):
        self.results = results  # Armazena os resultados das tabelas de frequência.

    def __str__(self):
        # Define a representação em string para a classe, formatando os resultados de forma legível.
        output = []  # Lista para armazenar as strings de saída.

        for key, value in self.results.items():
            # Itera pelos resultados, onde `key` é o identificador da coluna ou grupo,
            # e `value` contém a tabela e os intervalos de classes.
            output.append(f"--- {key} ---")  # Adiciona um cabeçalho para cada tabela.

            output.append("Table:")
            table = value["table"].reset_index(drop=True)  
            # Reseta os índices da tabela para evitar inconsistências com a numeração original.
            table.index += 1  
            # Ajusta os índices para começar em 1.
            output.append(table.to_string(index=True, header=True))  
            # Adiciona a tabela formatada com cabeçalhos e índices ajustados.

            # Formatação dos intervalos (breaks) com cabeçalho.
            output.append("\nBreaks:")
            breaks_df = pd.DataFrame([value["breaks"]], columns=["start", "end", "h", "right"])  
            # Cria um DataFrame com os intervalos formatados.
            output.append(breaks_df.to_string(index=False, header=True))  
            # Adiciona os intervalos formatados sem índices.

            output.append("")  # Linha vazia para separar os grupos.

        return "\n".join(output)  # Junta todas as partes formatadas em uma única string.

def fdt_data_frame(x, k=None, by=None, breaks="Sturges", right=False, na_rm=False):
    """
    Cria tabelas de distribuição de frequência para as colunas numéricas de um DataFrame.

    Parâmetros:
    - x: DataFrame de entrada.
    - k: Número de classes. Se não especificado, será calculado com base no método `breaks`.
    - by: Nome da coluna para agrupar os dados (deve ser categórica ou objeto).
    - breaks: Método para calcular o número de classes ('Sturges', 'Scott', 'FD').
    - right: Indica se os intervalos incluem o limite direito. Padrão: False.
    - na_rm: Remove valores ausentes (<NA>) se True. Padrão: False.

    Retorna:
    - FDTResult: Um objeto personalizado contendo as tabelas de distribuição de frequência.
    """
    if not isinstance(x, pd.DataFrame):
        raise ValueError("Input x must be a DataFrame.")
        # Verifica se a entrada `x` é um DataFrame. Caso contrário, lança um erro.

    results = {}  # Dicionário para armazenar os resultados das tabelas.

    if by is None:
        # Se `by` não é especificado, processa todas as colunas numéricas do DataFrame.
        for column in x.select_dtypes(include=[np.number]).columns:
            # Itera sobre as colunas numéricas.
            column_data = x[column].dropna() if na_rm else x[column]
            # Remove valores ausentes se `na_rm` for True.
            fdt_result = make_fdt_multiple(column_data, k=k, breaks=breaks, right=right, na_rm=na_rm)
            # Gera a tabela de distribuição de frequência para a coluna atual.
            results[column] = {"table": fdt_result["table"], "breaks": fdt_result["breaks"]}
            # Armazena a tabela e os intervalos no dicionário de resultados.
    else:
        # Se `by` é especificado, agrupa os dados pela coluna indicada.
        if by not in x.columns:
            raise ValueError(f"Column '{by}' not found in the DataFrame.")
            # Verifica se a coluna de agrupamento existe no DataFrame. Caso contrário, lança um erro.
        if not pd.api.types.is_categorical_dtype(x[by]) and not pd.api.types.is_object_dtype(x[by]):
            raise ValueError(f"Column '{by}' must be categorical or of type object.")
            # Verifica se a coluna de agrupamento é categórica ou do tipo objeto. Caso contrário, lança um erro.

        grouped = x.groupby(by)
        # Agrupa o DataFrame pela coluna especificada.

        for group_name, group_data in grouped:
            # Itera sobre cada grupo gerado pelo agrupamento.
            for column in group_data.select_dtypes(include=[np.number]).columns:
                # Itera sobre as colunas numéricas de cada grupo.
                column_data = group_data[column].dropna() if na_rm else group_data[column]
                # Remove valores ausentes se `na_rm` for True.
                fdt_result = make_fdt_multiple(column_data, k=k, breaks=breaks, right=right, na_rm=na_rm)
                # Gera a tabela de distribuição de frequência para a coluna atual do grupo.
                results[f"{group_name}.{column}"] = {"table": fdt_result["table"], "breaks": fdt_result["breaks"]}
                # Armazena os resultados no dicionário, identificando pelo grupo e pela coluna.

    return FDTResult(results)
    # Retorna um objeto `FDTResult` contendo todas as tabelas e intervalos gerados.
