import pandas as pd
from make_fdt_format_classes import make_fdt_format_classes

def print_fdt_default(x, columns=range(6), round=2, format_classes=False, 
                      pattern="{:09.3e}", row_names=False, right=True, **kwargs):
    # Recupera o elemento table dentro de x
    res = x['table']

    # Arredonda os valores das colunas de 1 a 5
    res.iloc[:, 1:6] = res.iloc[:, 1:6].round(round) 
    # Concatena a coluna 0 com as demais colunas
    res = pd.concat([res.iloc[:, [0]], res.iloc[:, 1:6]], axis=1)
    
    # Filtra as colunas
    res = res.iloc[:, columns]

    # Acessa o elemento right dentro de x -> breaks, e o converte para booleano
    right_tmp = bool(x['breaks']['right'])

    # Faz a formatação das classes caso format_classes seja verdadeiro
    if format_classes:
        res.iloc[:, 0] = make_fdt_format_classes(res.iloc[:, 0].astype(str), right_tmp, pattern)

    columns_names = ['Class limits', 'f', 'rf', 'rf(%)', 'cf', 'cf(%)']
    res.columns = [columns_names[i] for i in columns]

    if row_names:
        print(res, **kwargs)
    else:
        print(res.to_string(index=False), **kwargs)