from fdt_cat_matrix import fdt_cat_matrix
import numpy as np
import pandas as pd
"""
# Test 1
x = np.array([
    ["A", "B", "C"],
    ["A", "B", "C"],
    ["B", "A", "C"],
    ["C", "A", "B"]
])
df = pd.DataFrame(x, columns=["Col1", "Col2", "Col3"])
res = fdt_cat_matrix(df, sort=True, decreasing=True)
print(res)

# Test 2
x = np.array([
    ["X", "Y", "Z"],
    ["X", "Y", "Z"],
    ["X", "Y", "Z"],
    ["X", "Y", "Z"]
])
df = pd.DataFrame(x, columns=["Col1", "Col2", "Col3"])
res = fdt_cat_matrix(df, sort=True, decreasing=True)
print(res)
"""
# Test 3
x = np.array([
    ["Dog", "Cat", "Fish"],
    ["Dog", "Dog", "Bird"],
    ["Cat", "Cat", "Fish"],
    ["Fish", "Dog", "Bird"]
])
df = pd.DataFrame(x, columns=["Col1", "Col2", "Col3"])
res = fdt_cat_matrix(df, sort=True, decreasing=False)
print(res)

