import pandas as pd

def print_fdt_cat_default(x, columns=range(6), round=2, row_names=False, right=True, **kwargs):
    # Concatena a linha 0 com as linhas 1 a 5 (arredondadas)
    res = pd.concat([x.iloc[:, [0]], x.iloc[:, 1:6].round(round)], axis=1)
    # Filtra as colunas
    res = res.iloc[:, columns]

    # Nomeia as colunas
    columns_names = columns_names = ['Category', 'f', 'rf', 'rf(%)', 'cf', 'cf(%)']
    res.columns = [columns_names[i] for i in columns]

    if row_names:
       print(res, **kwargs)
    else:
       print(res.to_string(index=False), **kwargs)