from make_fdt_cat_simple import make_fdt_cat_simple
def fdt_cat_default(x, sort=True, decreasing=True):
    """
    Função principal para criar uma tabela de distribuição de frequência para dados categóricos.

    Parâmetros:
    x (list ou pd.Series): Dados de entrada (lista ou Series do pandas).
    sort (bool): Se True, ordena a tabela pela frequência. Padrão é True.
    decreasing (bool): Se sort for True, ordena de forma decrescente (True) ou crescente (False). Padrão é True.

    Retorna:
    pd.DataFrame: Um DataFrame contendo a tabela de distribuição de frequência.
    """
    # Chama a função make_fdt_cat_simple para criar a tabela de frequência
    res = make_fdt_cat_simple(x, sort=sort, decreasing=decreasing)

    # Adiciona atributos de classe como metadados (opcional, apenas para rastreamento)
    res.attrs = {
        "class": ["fdt_cat_default", "fdt_cat", "data.frame"]
    }

    # Retorna o DataFrame resultante
    return res

