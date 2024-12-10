import pandas as pd
from make_fdt_cat_simple import make_fdt_cat_simple  # Supondo que essa função já esteja implementada

class FDTMatrixResult:
    """
    Classe para encapsular os resultados das tabelas de frequência para cada coluna 
    em uma matriz ou DataFrame e fornecer saída formatada.

    Atributos:
        results (dict): Dicionário onde as chaves são os nomes das colunas e os valores
                        são DataFrames contendo as tabelas de frequência respectivas.
    """
    def __init__(self, results):
        """
        Inicializa a classe com os resultados calculados.

        Parâmetros:
            results (dict): Dicionário de tabelas de frequência para colunas categóricas.
        """
        self.results = results

    def __str__(self):
        """
        Fornece uma representação de string formatada dos resultados das tabelas de frequência,
        com linhas numeradas para melhor legibilidade.

        Retorna:
            str: Uma string formatada contendo as tabelas de frequência para cada coluna categórica.
        """
        output = []
        for key, value in self.results.items():
            if key == "class":
                continue  # Ignora metadados, se existirem
            output.append(f"--- {key} ---")  # Nome da coluna
            output.append("Table:")
            # Adiciona índice (começando de 1) para enumerar a tabela
            value_with_index = value.reset_index(drop=True).copy()
            value_with_index.index += 1  # Faz o índice começar de 1
            table_with_index = value_with_index.to_string(index=True)  # Mostra o índice
            output.append(table_with_index)
            output.append("")  # Linha em branco entre as tabelas
        return "\n".join(output)

def fdt_cat_matrix(x, sort=True, decreasing=True):
    """
    Cria tabelas de distribuição de frequência (FDTs) para cada coluna em uma matriz ou DataFrame.

    Parâmetros:
        x (np.ndarray ou pd.DataFrame): Matriz ou DataFrame, onde cada coluna é tratada como dados categóricos.
        sort (bool): Se True, ordena a tabela de cada coluna por frequência. Padrão é True.
        decreasing (bool): Se sort for True, ordena em ordem decrescente (True) ou crescente (False). Padrão é True.

    Retorna:
        FDTMatrixResult: Um objeto contendo as tabelas de frequência para todas as colunas.
    """
    # Verifica se a entrada é um DataFrame ou Series
    if not isinstance(x, (pd.DataFrame, pd.Series)):
        raise ValueError("A entrada deve ser um DataFrame ou Series do pandas.")

    # Converte Series em DataFrame, se necessário
    if isinstance(x, pd.Series):
        x = x.to_frame()  # Converte Series para DataFrame com uma coluna

    results = {}

    # Itera sobre as colunas do DataFrame
    for col_name in x.columns:
        column_data = x[col_name]
        # Chama make_fdt_cat_simple para gerar a tabela de frequência
        fdt = make_fdt_cat_simple(column_data, sort=sort, decreasing=decreasing)
        results[col_name] = fdt

    # Retorna os resultados encapsulados na classe FDTMatrixResult
    return FDTMatrixResult(results)

