import numpy as np
from make_fdt_simple import make_fdt_simple


# Test 1: Basic intervals
x = np.array([5, 10, 15, 20, 25, 30, 35])
start = 0
end = 40
h = 10
print("Test 1 - Basic intervals")
print(make_fdt_simple(x, start, end, h))
"""
# Test 2: Overlapping intervals (right=TRUE)
x = np.array([5, 7, 10, 13, 15, 18, 20])
start = 0
end = 20
h = 5
print("\nTest 2 - Overlapping intervals (right=True)")
print(make_fdt_simple(x, start, end, h, right=True))

# Test 3: Data exceeding the defined interval
x = np.array([5, 12, 19, 26, 33, 40, 47])
start = 0
end = 50
h = 10
print("\nTest 3 - Data exceeding the defined interval")
print(make_fdt_simple(x, start, end, h))

# Test 4: Uniform data
x = np.array([10, 10, 10, 10, 10])
start = 0
end = 20
h = 5
print("\nTest 4 - Uniform data")
print(make_fdt_simple(x, start, end, h))

# Test 5: Small class width
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
start = 0
end = 3
h = 0.5
print("\nTest 5 - Small class width")
print(make_fdt_simple(x, start, end, h))
"""
