from make_fdt_cat_simple import make_fdt_cat_simple

# Tests for the make_fdt_cat_simple function

x1 = ["A", "B", "A", "C", "B", "B", "C", "A", "C", "C"]
x2 = ["X", "Y", "X", "Z", "Y", "Y", "Z", "Z", "Z", "Z"]
x3 = ["Red", "Blue", "Green", "Red", "Green", "Blue", "Blue", "Green"]

# Test 1
print("Test 1 - Python")
print(make_fdt_cat_simple(x1, sort=True, decreasing=True))

# Test 2
print("\nTest 2 - Python")
print(make_fdt_cat_simple(x2, sort=False, decreasing=False))

# Test 3
print("\nTest 3 - Python")
print(make_fdt_cat_simple(x3, sort=True, decreasing=False))
