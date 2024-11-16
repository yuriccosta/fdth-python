import numpy as np
import pandas as pd
from make_fdt_multiple import make_fdt_multiple


class FDTMatrixResult:
    """
    Class to encapsulate the results of frequency distribution tables for matrices
    and provide formatted output.
    """
    def __init__(self, results):
        self.results = results

    def __str__(self):
        output = []
        for key, value in self.results.items():
            output.append(f"--- {key} ---")
            output.append("Table:")
            output.append(value["table"].to_string(index=False))  # Format table as string
            output.append("\nBreaks:")
            for break_key, break_value in value["breaks"].items():
                output.append(f"  {break_key}: {break_value}")
            output.append("")  # Empty line to separate sections
        return "\n".join(output)


def fdt_matrix(x, k=None, breaks="Sturges", right=False, na_rm=False):
    """
    Generate frequency distribution tables for each column of a matrix.

    Parameters:
    x (numpy.ndarray): Input matrix with numerical data.
    k (int, optional): Number of classes for the histogram. Defaults to None.
    breaks (str, optional): Method to calculate the number of classes ('Sturges', 'Scott', 'FD').
    right (bool, optional): Whether to include the right endpoint in each interval. Defaults to False.
    na_rm (bool, optional): Whether to remove NA values from the data. Defaults to False.

    Returns:
    FDTMatrixResult: A custom object containing the frequency distribution tables.
    """
    if not isinstance(x, np.ndarray):
        raise ValueError("Input x must be a numpy.ndarray.")
    
    results = {}

    # Iterate through each column of the matrix
    for i in range(x.shape[1]):
        col_data = x[:, i]

        # Call make_fdt_multiple for each column
        fdt_result = make_fdt_multiple(col_data, k=k, breaks=breaks, right=right, na_rm=na_rm)
        
        # Store results in a dictionary
        col_name = f"Column:{i+1}"
        results[col_name] = {"table": fdt_result["table"], "breaks": fdt_result["breaks"]}

    return FDTMatrixResult(results)
