import pandas as pd
from make_fdt_cat_multiple import make_fdt_cat_multiple


class FDTResultMultiple:
    """
    Class to encapsulate the results of frequency distribution tables (FDTs) 
    for multiple columns and provide formatted output.
    """
    def __init__(self, results):
        """
        Initialize the FDTResultMultiple class with the computed results.

        Parameters:
            results (dict): A dictionary where keys are column or group-column names 
                            and values are DataFrames containing the FDT for each case.
        """
        self.results = results

    def __str__(self):
        """
        Provide a formatted string representation of the FDT results.

        Returns:
            str: A formatted string containing the FDT for each column or group.
        """
        output = []
        for key, value in self.results.items():
            output.append(f"--- {key} ---")
            output.append("Table:")
            output.append(value.to_string(index=True))
            output.append("")
        return "\n".join(output)


def fdt_cat_data_frame(df, by=None, sort=True, decreasing=True):
    """
    Generate frequency distribution tables (FDTs) for categorical columns in a DataFrame, 
    optionally grouped by a specified column.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        by (str, optional): Column name to group the data by. Default is None.
        sort (bool): If True, sort the FDT by frequency. Default is True.
        decreasing (bool): If sort is True, sorts in descending order if True, 
                           otherwise in ascending order. Default is True.

    Returns:
        FDTResultMultiple: An object containing the FDTs for all relevant columns.

    Raises:
        ValueError: If the input is not a DataFrame, the grouping column is not present, 
                    or the grouping column is not categorical.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The parameter 'df' must be a pandas DataFrame.")

    results = {}

    if by is None:
        # If no grouping column is specified
        categorical_columns = df.select_dtypes(include=['category', 'object']).columns
        for col in categorical_columns:
            fdt = make_fdt_cat_multiple(df[[col]], sort=sort, decreasing=decreasing)
            results[col] = fdt.results[col]
    else:
        # If a grouping column is specified
        if by not in df.columns:
            raise ValueError(f"The column '{by}' is not present in the DataFrame.")
        if not pd.api.types.is_categorical_dtype(df[by]) and not pd.api.types.is_object_dtype(df[by]):
            raise ValueError(f"The column '{by}' must be categorical.")

        # Avoid FutureWarning for groupby
        groups = df.groupby(by, observed=False)
        for group_name, group_data in groups:
            group_df = group_data.drop(columns=by)
            categorical_columns = group_df.select_dtypes(include=['category', 'object']).columns
            for col in categorical_columns:
                fdt = make_fdt_cat_multiple(group_df[[col]], sort=sort, decreasing=decreasing)
                results[f"{group_name}.{col}"] = fdt.results[col]

    return FDTResultMultiple(results)
