import pandas as pd

def make_fdt_cat_simple(x, sort=False, decreasing=False):
    """
    Creates a frequency distribution table (FDT) for categorical data.

    Parameters:
    x (list or pd.Series): The input data, which must be a list or pandas Series.
    sort (bool): If True, sorts the table by frequency. Default is False.
    decreasing (bool): If sort is True, sorts in descending order if True, otherwise in ascending order. Default is False.

    Returns:
    pd.DataFrame: A DataFrame containing the following columns:
        - 'Category': The unique categories.
        - 'f': The absolute frequency of each category.
        - 'rf': The relative frequency of each category.
        - 'rf(%)': The relative frequency expressed as a percentage.
        - 'cf': The cumulative absolute frequency.
        - 'cf(%)': The cumulative relative frequency expressed as a percentage.
    """
    if not isinstance(x, (pd.Series, list)):
        raise ValueError("Input data must be a list or pandas Series.")

    # Convert to pandas Series if it's a list
    x = pd.Series(x)
    
    if not (x.dtypes == 'object' or x.dtypes.name == 'category'):
        raise ValueError("Values must be strings or categorical.")

    # Convert to categorical type
    x = x.astype('category')

    # Calculate absolute frequency
    f = x.value_counts(sort=False)

    if sort:
        # Sort by absolute frequencies
        f = f.sort_values(ascending=not decreasing)

    # Calculate relative frequencies and cumulative frequencies
    rf = f / f.sum()             # Relative frequency
    rfp = rf * 100               # Relative frequency as a percentage
    cf = f.cumsum()              # Cumulative absolute frequency
    cfp = rfp.cumsum()           # Cumulative relative frequency as a percentage

    # Create the final table
    res = pd.DataFrame({
        'Category': f.index,
        'f': f.values,
        'rf': rf.values,
        'rf(%)': rfp.values,
        'cf': cf.values,
        'cf(%)': cfp.values
    })

    return res
