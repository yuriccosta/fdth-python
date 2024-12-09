import pandas as pd
from fdt_cat_data_frame import fdt_cat_data_frame  # Ensure the function and class are in the same directory


# Test 1: Without grouping
df1 = pd.DataFrame({
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y'])
})
result1 = fdt_cat_data_frame(df1, sort=True, decreasing=True)
print(result1)
"""
# Test 2: With grouping
df2 = pd.DataFrame({
    'group': pd.Categorical(['G1', 'G1', 'G2', 'G2', 'G2']),
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y'])
})
result2 = fdt_cat_data_frame(df2, by='group', sort=True, decreasing=False)
print(result2)

# Test 3: With numeric column
df3 = pd.DataFrame({
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y']),
    'col3': [1, 2, 3, 4, 5]  # Numeric column
})
result3 = fdt_cat_data_frame(df3, sort=False)
print(result3)
"""

