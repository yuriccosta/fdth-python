import pandas as pd
from make_fdt_cat_multiple import make_fdt_cat_multiple

class FDTResultMultiple:
    """
    Classe para encapsular os resultados das tabelas de frequência (FDTs) 
    para múltiplas colunas e fornecer saída formatada.
    """
    def __init__(self, results):
        """
        Inicializa a classe com os resultados calculados.

        Parâmetros:
            results (dict): Dicionário onde as chaves são nomes de colunas ou grupos 
                            e os valores são DataFrames contendo as tabelas de frequência.
        """
        self.results = results

    def __str__(self):
        """
        Fornece uma representação de string formatada dos resultados das tabelas de frequência.

        Retorna:
            str: Uma string formatada contendo as tabelas de frequência.
        """
        output = []
        for key, value in self.results.items():
            output.append(f"--- {key} ---")  # Nome da coluna ou grupo
            output.append("Table:")
            output.append(value.to_string(index=True))  # Mostra a tabela
            output.append("")  # Linha em branco entre os grupos
        return "\n".join(output)

def fdt_cat_data_frame(df, by=None, sort=True, decreasing=True):
    """
    Gera tabelas de frequência para colunas categóricas em um DataFrame, 
    opcionalmente agrupadas por uma coluna específica.

    Parâmetros:
        df (pd.DataFrame): DataFrame de entrada.
        by (str, opcional): Nome da coluna para agrupar os dados. Padrão é None.
        sort (bool): Se True, ordena as tabelas pela frequência. Padrão é True.
        decreasing (bool): Se sort for True, ordena em ordem decrescente (True) ou crescente (False). Padrão é True.

    Retorna:
        FDTResultMultiple: Um objeto contendo as tabelas de frequência para todas as colunas relevantes.

    Levanta:
        ValueError: Se a entrada não for um DataFrame ou se a coluna de agrupamento for inválida.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("O parâmetro 'df' deve ser um DataFrame do pandas.")

    results = {}

    if by is None:
        # Processa todas as colunas categóricas
        categorical_columns = df.select_dtypes(include=['category', 'object']).columns
        for col in categorical_columns:
            fdt = make_fdt_cat_multiple(df[[col]], sort=sort, decreasing=decreasing)
            results[col] = fdt.results[col]
    else:
        # Processa dados agrupados por uma coluna
        if by not in df.columns:
            raise ValueError(f"A coluna '{by}' não está presente no DataFrame.")
        if not pd.api.types.is_categorical_dtype(df[by]) and not pd.api.types.is_object_dtype(df[by]):
            raise ValueError(f"A coluna '{by}' deve ser categórica.")

        # Agrupa os dados e cria tabelas para cada grupo
        groups = df.groupby(by, observed=False)
        for group_name, group_data in groups:
            group_df = group_data.drop(columns=by)
            categorical_columns = group_df.select_dtypes(include=['category', 'object']).columns
            for col in categorical_columns:
                fdt = make_fdt_cat_multiple(group_df[[col]], sort=sort, decreasing=decreasing)
                results[f"{group_name}.{col}"] = fdt.results[col]

    return FDTResultMultiple(results)
