from fdt_data_frame import fdt_data_frame
import pandas as pd

# Test 1: A simple DataFrame with a single numeric column
"""
df1 = pd.DataFrame({
    "A": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
})
result1 = fdt_data_frame(df1)
print(result1)

# Test 2: A DataFrame with two numeric columns
df2 = pd.DataFrame({
    "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "B": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
})
print("\nTest 2 (without grouping):")
result2 = fdt_data_frame(df2)
print(result2)

# Test 3: DataFrame with grouping
df3 = pd.DataFrame({
    "A": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    "B": [10, 20, 20, 30, 30, 30, 40, 40, 40, 40],
    "Group": ["G1", "G1", "G1", "G1", "G2", "G2", "G2", "G2", "G2", "G2"]
})
result3 = fdt_data_frame(df3, by="Group")
print(result3)
"""
# Test 3: DataFrame with grouping
df1 = pd.DataFrame({
    "A": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
})
result1 = fdt_data_frame(df1)
print(result1)