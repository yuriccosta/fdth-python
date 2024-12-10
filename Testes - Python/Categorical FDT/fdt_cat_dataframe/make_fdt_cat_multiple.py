import pandas as pd
from make_fdt_cat_simple import make_fdt_cat_simple

class FDTResult:
    """
    Class to encapsulate the results of frequency distribution tables (FDTs) 
    and provide formatted output.

    Attributes:
        results (dict): A dictionary where keys are column names and values are
                        DataFrames containing the FDT for the respective columns.
    """
    def __init__(self, results):
        """
        Initialize the FDTResult class with the computed results.

        Parameters:
            results (dict): Dictionary of FDTs for categorical columns.
        """
        self.results = results

    def __str__(self):
        """
        Provide a formatted string representation of the FDT results.

        Returns:
            str: A formatted string containing the FDT for each categorical column.
        """
        output = []
        for key, value in self.results.items():
            output.append(f"--- {key} ---")
            output.append("Table:")
            table_with_index = value.to_string(index=True)  
            output.append(table_with_index)
            output.append("")  
        return "\n".join(output)


def make_fdt_cat_multiple(df, sort=False, decreasing=False):
    """
    Create frequency distribution tables (FDTs) for all categorical columns in a DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        sort (bool): If True, sorts the tables by frequency. Default is False.
        decreasing (bool): If sort is True, sorts in descending order if True, 
                           otherwise in ascending order. Default is False.

    Returns:
        FDTResult: An object containing FDTs for all categorical columns.

    Raises:
        ValueError: If the input is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The parameter 'df' must be a pandas DataFrame.")

    results = {}
    # Select only categorical columns
    categorical_columns = df.select_dtypes(include=['category', 'object']).columns

    for col in categorical_columns:
        column_data = df[col]
        fdt = make_fdt_cat_simple(column_data, sort=sort, decreasing=decreasing)
        results[col] = fdt

    return FDTResult(results)
