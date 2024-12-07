import pandas as pd

def summary_fdt_cat_default(object, columns=range(6), round=2, row_names=False, right=True, **kwargs):
   # Concatena a linha 0 com as linhas 1 a 5 (arredondadas)
    res = pd.concat([object.iloc[:, [0]], object.iloc[:, 1:6].round(round)], axis=1)
    # Filtra as colunas
    res = res.iloc[:, columns]

    # Nomeia as colunas
    columns_names = columns_names = ['Category', 'f', 'rf', 'rf(%)', 'cf', 'cf(%)']
    res.columns = [columns_names[i] for i in columns]

    if row_names:
       print(res, **kwargs)
    else:
       print(res.to_string(index=False), **kwargs)

    return res