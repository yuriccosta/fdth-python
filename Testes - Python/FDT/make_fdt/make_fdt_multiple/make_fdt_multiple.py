import numpy as np
from make_fdt_simple import make_fdt_simple

def make_fdt_multiple(x, k=None, breaks="Sturges", right=False, na_rm=False):
    """
    Create a multiple frequency distribution table.

    Parameters:
    x (array-like): The data array.
    k (int, optional): Number of classes. If not provided, it will be calculated based on `breaks`.
    breaks (str, optional): Method to calculate the number of classes ('Sturges', 'Scott', 'FD').
    right (bool, optional): Whether to include the right endpoint in each interval.
    na_rm (bool, optional): Whether to remove NA values from the data.

    Returns:
    dict: A dictionary with the frequency table and breakpoints information.
    """
    if not na_rm and np.isnan(x).any():
        raise ValueError("The data has <NA> values and na_rm=False by default.")
    
    # Remove NA values if na_rm is True
    x = np.array(x)
    if na_rm:
        x = x[~np.isnan(x)]
    
    def nclass_scott(data):
        h = 3.5 * np.std(data) * len(data) ** (-1/3)
        if h > 0:
            return max(1, int(np.ceil((data.max() - data.min()) / h)))
        return 1

    def nclass_fd(data):
        h = 2 * np.subtract(*np.percentile(data, [75, 25]))
        if h == 0:
            sorted_data = np.sort(data)
            alpha = 0.25
            min_alpha = 1 / 512
            while h == 0 and alpha >= min_alpha:
                h = (np.percentile(sorted_data, 100 - alpha * 100) - 
                     np.percentile(sorted_data, alpha * 100)) / (1 - 2 * alpha)
                alpha /= 2
        if h == 0:
            h = 3.5 * np.std(data)
        if h > 0:
            return int(np.ceil((data.max() - data.min()) / h * len(data) ** (1/3)))
        return 1
    
    # Determine k if not provided
    if k is None:
        if breaks == "Sturges":
            k = int(np.ceil(np.log2(len(x)) + 1))
        elif breaks == "Scott":
            k = nclass_scott(x)
        elif breaks == "FD":
            k = nclass_fd(x)
        else:
            raise ValueError(f"Unknown method for breaks: {breaks}")

    # Compute the class interval and range
    start = x.min() - abs(x.min()) / 100
    end = x.max() + abs(x.max()) / 100
    R = end - start
    h = R / k

    # Call the simple FDT function
    fdt_table = make_fdt_simple(x, start, end, h, right)
    
    breaks_info = {
        "start": start,
        "end": end,
        "h": h,
        "right": int(right)
    }

    return {"table": fdt_table, "breaks": breaks_info}


