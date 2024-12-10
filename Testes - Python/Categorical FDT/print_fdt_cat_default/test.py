from print_fdt_cat_default import print_fdt_cat_default
from fdt_cat_default import fdt_cat_default

# Exemplo de uso: vetor categórico
categorias = [
    "Masculino", "Feminino", "Feminino", "Masculino", "Masculino", 
    "Feminino", "Outro", "Masculino", "Feminino", "Outro", 
    "Feminino", "Masculino", "Outro", "Masculino", "Feminino", 
    "Masculino", "Outro", "Feminino", "Outro", "Feminino", 
    "Masculino", "Outro", "Feminino", "Outro", "Masculino", 
    "Feminino", "Masculino", "Outro", "Outro", "Feminino"
]

tdf_categorias = fdt_cat_default(x = categorias)
print(f"TDF Categorica 1\n")
print_fdt_cat_default(x = tdf_categorias, columns = [0, 1, 3, 4], round=2, row_names=False, right=False)
print()

# Exemplo de vetor categórico com números e texto
categorias2 = [
    "A", "B", "C", 1, 2, 3, "A", 1, "C", "B",
    2, "A", "C", 3, "B", 1, "C", "A", 2, 3,
    "B", 1, "C", 2, "A", "B", 3, "C", 1, 2
]

tdf_categorias2 = fdt_cat_default(categorias2)
print(f"TDF Categorica 2\n")
print_fdt_cat_default(x = tdf_categorias2, round=2)
print()