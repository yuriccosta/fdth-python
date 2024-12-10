import numpy as np
from fdt_matrix import fdt_matrix  


# Input matrix for testing
data_matrix = np.array([
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40],
    [5, 50]
])
"""
# Test with a specified number of classes
result_k3 = fdt_matrix(data_matrix, k=3, right=False, na_rm=False)
print(result_k3)

# Test with breaks='Sturges'
result_sturges = fdt_matrix(data_matrix, breaks="Sturges", right=False, na_rm=False)
print(result_sturges)

# Test with breaks='Scott'
result_scott = fdt_matrix(data_matrix, breaks="Scott", right=False, na_rm=False)
print(result_scott)

# Test with breaks='FD'
result_fd = fdt_matrix(data_matrix, breaks="FD", right=False, na_rm=False)
print(result_fd)

# Test with right=True
result_right = fdt_matrix(data_matrix, k=3, right=True, na_rm=False)
print(result_right)
"""
# Test with a specified number of classes
result_k3 = fdt_matrix(data_matrix, k=3, right=False, na_rm=False)
print(result_k3)