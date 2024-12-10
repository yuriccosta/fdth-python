import pandas as pd
from make_fdt_cat_multiple import make_fdt_cat_multiple

# Test Data 1
data = {
    "col1": ["A", "B", "A", "C", "B", "B", "C", "A", "C", "C"],
    "col2": ["X", "Y", "X", "Z", "Y", "Y", "Z", "Z", "Z", "Z"]
}

df = pd.DataFrame(data)
df["col1"] = df["col1"].astype("category")
df["col2"] = df["col2"].astype("category")

# Execute Test 1
result = make_fdt_cat_multiple(df, sort=True, decreasing=True)
print(result)

# Test Data 2
data = {
    "col1": ["Red", "Blue", "Red", "Green", "Blue", "Blue", "Green", "Red", "Green", "Green"],
    "col2": ["Dog", "Cat", "Dog", "Bird", "Cat", "Cat", "Bird", "Bird", "Bird", "Bird"],
    "col3": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Non-categorical
}

df = pd.DataFrame(data)
df["col1"] = df["col1"].astype("category")
df["col2"] = df["col2"].astype("category")

# Execute Test 2
result = make_fdt_cat_multiple(df, sort=False, decreasing=False)
print(result)

# Test Data 3
data = {
    "col1": ["Apple", "Apple", "Banana", "Banana", "Banana", "Grape", "Grape", "Apple", "Apple", "Grape"],
    "col2": ["Small", "Small", "Large", "Large", "Large", "Small", "Small", "Large", "Large", "Large"],
    "col3": ["Low", "Low", "High", "High", "High", "Medium", "Medium", "Low", "Low", "Medium"]
}

df = pd.DataFrame(data)
df["col1"] = df["col1"].astype("category")
df["col2"] = df["col2"].astype("category")
df["col3"] = df["col3"].astype("category")

# Execute Test 3
result = make_fdt_cat_multiple(df, sort=True, decreasing=False)
print(result)
