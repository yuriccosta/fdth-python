from summary_fdt_default import summary_fdt_default
from fdt_default import fdt_default

x = [6.34, 4.57, 7.89, 5.12, 4.26, 5.77, 2.95, 8.13, 3.48, 6.05, 
     4.93, 6.88, 7.21, 3.69, 5.55, 2.87, 5.02, 4.31, 6.79, 3.98, 
     7.44, 5.36, 6.12, 4.59, 8.27, 3.65, 5.48, 7.81, 3.93, 5.67]

print(f"\nx = {x}\n")

tdf_x = fdt_default(x = x, breaks='Sturges')
print(f"TDF de X: \n{tdf_x}\n")

print("Exemplo com formatação de classes, seleção de colunas e nome de colunas")
summary_fdt_default(tdf_x, columns=[0,1,2], round=2, format_classes=True, pattern="{:02.3e}", row_names=True)
print()

print("Exemplo com seleção de colunas e formatação de classes")
col = [0, 3, 5]
summary_fdt_default(tdf_x, columns = col, format_classes = True, pattern = "{:.5e}")