import pandas as pd

def print_fdt_cat_default(x, columns=range(6), round=2, row_names=False, right=True, **kwargs):
    # Concatenate line 0 with lines 1 to 5 (rounded)
    res = pd.concat([x.iloc[:, [0]], x.iloc[:, 1:6].round(round)], axis=1)
    # Filters the columns
    res = res.iloc[:, columns]

    # Name the columns
    columns_names = columns_names = ['Category', 'f', 'rf', 'rf(%)', 'cf', 'cf(%)']
    res.columns = [columns_names[i] for i in columns]

    if row_names:
       print(res, **kwargs)
    else:
       print(res.to_string(index=False), **kwargs)
