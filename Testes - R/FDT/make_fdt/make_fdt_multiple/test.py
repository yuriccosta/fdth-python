from make_fdt_multiple import make_fdt_multiple

import pandas as pd
import numpy as np
"""
# Test 1
x_uniform = pd.Series([10, 15, 20, 25, 30, 35, 40])
result_uniform_python = make_fdt_multiple(x=x_uniform, breaks="Sturges", right=False, na_rm=True)
print(result_uniform_python["table"])
print(result_uniform_python["breaks"])

#Test 2
np.random.seed(42)
x_normal = pd.Series(np.random.normal(loc=20, scale=5, size=50))
result_normal_python = make_fdt_multiple(x=x_normal, breaks="FD", right=False, na_rm=True)
print(result_normal_python["table"])
print(result_normal_python["breaks"])

#Test 3
x_negative = pd.Series([-10, -5, 0, 5, 10])
result_negative_python = make_fdt_multiple(x=x_negative, k=5, right=False, na_rm=True)
print(result_negative_python["table"])
print(result_negative_python["breaks"])
"""
# Test 1
x_uniform = pd.Series([10, 15, 20, 25, 30, 35, 40])
result_uniform_python = make_fdt_multiple(x=x_uniform, breaks="Sturges", right=False, na_rm=True)
print(result_uniform_python["table"])
print(result_uniform_python["breaks"])