from make_fdt_cat_simple import make_fdt_cat_simple
def fdt_cat_default(object, sort=True, decreasing=True):
    """
    Main function to create a frequency distribution table for categorical data.

    Parameters:
    x (list or pd.Series): The input data, which must be a list or pandas Series.
    sort (bool): If True, sorts the table by frequency. Default is True.
    decreasing (bool): If sort is True, sorts in descending order if True, otherwise in ascending order. Default is True.

    Returns:
    pd.DataFrame: A DataFrame containing the frequency distribution table.
    """
    # Call the make_fdt_cat_simple function to create the table
    res = make_fdt_cat_simple(object, sort=sort, decreasing=decreasing)

    # Adding class attributes as metadata (optional, for traceability)
    res.attrs = {
        "class": ["fdt_cat_default", "fdt_cat", "data.frame"]
    }

    return res
