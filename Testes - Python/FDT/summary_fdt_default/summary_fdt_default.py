import pandas as pd
from make_fdt_format_classes import make_fdt_format_classes

def print_fdt_default(object, columns=range(6), round=2, format_classes=False,
                        pattern="{:09.3e}", row_names=False, right=True, **kwargs):
    # Retrieves the table element inside object
    res = object['table']

    # Rounds the values of columns from 1 to 5
    res.iloc[:, 1:6] = res.iloc[:, 1:6].round(round) 
    # Concatenate column 0 with the other columns 
    res = pd.concat([res.iloc[:, [0]], res.iloc[:, 1:6]], axis=1)
    
    # Filters the columns
    res = res.iloc[:, columns]

    # Accesses the right element within object -> breaks, and converts it to boolean
    right_tmp = bool(object['breaks']['right'])

    # Formats classes if format_classes is true
    if format_classes:
        res.iloc[:, 0] = make_fdt_format_classes(res.iloc[:, 0].astype(str), right_tmp, pattern)

    columns_names = ['Class limits', 'f', 'rf', 'rf(%)', 'cf', 'cf(%)']
    res.columns = [columns_names[i] for i in columns]

    if not right:
        # @TODO The left alignment needs to be implemented 
        pass

    if row_names:
        # If row_names is set as 'true', indexes will be printed
        print(res, **kwargs)
    else:
        # If row_names is set as 'false', indexes won't be printed
        print(res.to_string(index=False), **kwargs)

    return res