import numpy as np
from make_fdt_simple import make_fdt_simple

def fdt_default(x, k=None, start=None, end=None, h=None, breaks='Sturges', right=False, na_rm=False):
    """
    Generate a frequency distribution table (FDT) with specified or default bin settings.

    Parameters:
    x (array-like): The data array.
    k (int, optional): The number of bins/classes. If None, calculated based on 'breaks' method.
    start (float, optional): The start of the interval range.
    end (float, optional): The end of the interval range.
    h (float, optional): The class interval width.
    breaks (str, optional): Method for determining bins ('Sturges', 'Scott', 'FD'). Defaults to 'Sturges'.
    right (bool, optional): Whether to include the right endpoint in each interval. Defaults to False.
    na_rm (bool, optional): Remove missing values if True. Defaults to False.

    Returns:
    dict: A dictionary containing the frequency distribution table and binning details.
    """
    x = np.array([np.nan if v is None else v for v in x], dtype=np.float64)

    if not np.issubdtype(x.dtype, np.number):
        raise TypeError("The data vector must be numeric.")
    
    if na_rm:
        x = x[~np.isnan(x)]
    elif np.any(np.isnan(x)):
        raise ValueError("The data has <NA> values and na.rm=FALSE by default.")
    
    # Bin calculation based on specified method
    if k is None and start is None and end is None and h is None:
        if breaks == 'Sturges':
            k = int(np.ceil(1 + 3.322 * np.log10(len(x))))
        elif breaks == 'Scott':
            std_dev = np.std(x)
            k = int(np.ceil((x.max() - x.min()) / (3.5 * std_dev / (len(x) ** (1 / 3)))))
        elif breaks == 'FD':
            iqr = np.percentile(x, 75) - np.percentile(x, 25)
            k = int(np.ceil((x.max() - x.min()) / (2 * iqr / (len(x) ** (1 / 3)))))
        else:
            raise ValueError("Invalid 'breaks' method.")
        
        start, end = x.min() - abs(x.min()) / 100, x.max() + abs(x.max()) / 100
        R = end - start
        h = R / k

    elif start is None and end is None and h is None:
        start, end = x.min() - abs(x.min()) / 100, x.max() + abs(x.max()) / 100
        R = end - start
        h = R / k

    elif k is None and h is None:
        R = end - start
        k = int(np.sqrt(abs(R)))
        k = max(k, 5)
        h = R / k

    elif k is None:
        pass

    else:
        raise ValueError("Please check the function syntax!")
    
    # Generate the frequency distribution table
    table = make_fdt_simple(x, start, end, h, right)
    breaks_info = {'start': start, 'end': end, 'h': h, 'right': int(right)}
    result = {'table': table, 'breaks': breaks_info}
    
    return result
