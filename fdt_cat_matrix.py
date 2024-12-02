import pandas as pd
from make_fdt_cat_simple import make_fdt_cat_simple  # Supondo que essa função já esteja implementada

class FDTMatrixResult:
    """
    Class to encapsulate the results of frequency distribution tables (FDTs) 
    for each column in a matrix or DataFrame and provide formatted output.

    Attributes:
        results (dict): A dictionary where keys are column names and values are
                        DataFrames containing the FDT for the respective columns.
    """
    def __init__(self, results):
        """
        Initialize the FDTMatrixResult class with the computed results.

        Parameters:
            results (dict): Dictionary of FDTs for categorical columns.
        """
        self.results = results

    def __str__(self):
        """
        Provide a formatted string representation of the FDT results,
        with numbered rows for better readability.

        Returns:
            str: A formatted string containing the FDT for each categorical column.
        """
        output = []
        for key, value in self.results.items():
            if key == "class":
                continue  # Skip metadata if any
            output.append(f"--- {key} ---")
            output.append("Table:")
            # Add index (starting from 1) to the table for enumeration
            value_with_index = value.reset_index(drop=True).copy()
            value_with_index.index += 1  # Make index start from 1
            table_with_index = value_with_index.to_string(index=True)  # Show index
            output.append(table_with_index)
            output.append("")  # Blank line between tables
        return "\n".join(output)



def fdt_cat_matrix(x, sort=True, decreasing=True):
    """
    Create frequency distribution tables (FDTs) for each column in a matrix or DataFrame.

    Parameters:
        x (np.ndarray or pd.DataFrame): Input matrix or DataFrame, where each column is treated as categorical data.
        sort (bool): If True, sorts each column's table by frequency. Default is True.
        decreasing (bool): If sort is True, sorts in descending order if True, otherwise in ascending order. Default is True.

    Returns:
        FDTMatrixResult: An object containing FDTs for all columns.
    """
    if not isinstance(x, (pd.DataFrame, pd.Series)):
        raise ValueError("Input must be a pandas DataFrame or Series.")

    if isinstance(x, pd.Series):
        x = x.to_frame()  # Convert Series to single-column DataFrame

    results = {}
    for col_name in x.columns:
        column_data = x[col_name]
        fdt = make_fdt_cat_simple(column_data, sort=sort, decreasing=decreasing)
        results[col_name] = fdt

    return FDTMatrixResult(results)
