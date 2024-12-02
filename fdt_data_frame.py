import pandas as pd
import numpy as np
from make_fdt_multiple import make_fdt_multiple


class FDTResult:
    """
    Class to encapsulate the results of frequency distribution tables and provide formatted output.
    """
    def __init__(self, results):
        self.results = results

    def __str__(self):
        output = []
        for key, value in self.results.items():
            output.append(f"--- {key} ---")
            output.append("Table:")
            output.append(value["table"].to_string(index=False))  # Convert the table to a readable string
            output.append("\nBreaks:")
            for break_key, break_value in value["breaks"].items():
                output.append(f"  {break_key}: {break_value}")
            output.append("")  # Empty line to separate groups
        return "\n".join(output)


def fdt_data_frame(x, k=None, by=None, breaks="Sturges", right=False, na_rm=False):
    """
    Create frequency distribution tables for numeric columns in a DataFrame.

    Parameters:
    x (DataFrame): Input data.
    k (int, optional): Number of classes. If not provided, it will be calculated based on `breaks`.
    by (str, optional): Column name to group by (must be a factor/categorical column).
    breaks (str, optional): Method to calculate the number of classes ('Sturges', 'Scott', 'FD').
    right (bool, optional): Whether to include the right endpoint in each interval.
    na_rm (bool, optional): Whether to remove NA values from the data.

    Returns:
    FDTResult: A custom object containing the frequency distribution tables.
    """
    if not isinstance(x, pd.DataFrame):
        raise ValueError("Input x must be a DataFrame.")

    results = {}

    if by is None:
        # Process all numeric columns
        for column in x.select_dtypes(include=[np.number]).columns:
            column_data = x[column].dropna() if na_rm else x[column]
            fdt_result = make_fdt_multiple(column_data, k=k, breaks=breaks, right=right, na_rm=na_rm)
            results[column] = {"table": fdt_result["table"], "breaks": fdt_result["breaks"]}
    else:
        # Group by the specified column and process numeric columns in each group
        if by not in x.columns:
            raise ValueError(f"Column '{by}' not found in the DataFrame.")
        if not pd.api.types.is_categorical_dtype(x[by]) and not pd.api.types.is_object_dtype(x[by]):
            raise ValueError(f"Column '{by}' must be categorical or of type object.")

        grouped = x.groupby(by)
        for group_name, group_data in grouped:
            for column in group_data.select_dtypes(include=[np.number]).columns:
                column_data = group_data[column].dropna() if na_rm else group_data[column]
                fdt_result = make_fdt_multiple(column_data, k=k, breaks=breaks, right=right, na_rm=na_rm)
                results[f"{group_name}.{column}"] = {"table": fdt_result["table"], "breaks": fdt_result["breaks"]}

    return FDTResult(results)
