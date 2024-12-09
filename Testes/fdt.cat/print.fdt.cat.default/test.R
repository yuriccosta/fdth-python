library("fdth")

categorias <- c(
  "Masculino", "Feminino", "Feminino", "Masculino", "Masculino", 
  "Feminino", "Outro", "Masculino", "Feminino", "Outro", 
  "Feminino", "Masculino", "Outro", "Masculino", "Feminino", 
  "Masculino", "Outro", "Feminino", "Outro", "Feminino", 
  "Masculino", "Outro", "Feminino", "Outro", "Masculino", 
  "Feminino", "Masculino", "Outro", "Outro", "Feminino")

tdf_categorias <- fdt_cat(categorias)
cat("TDF Categorica 1\n\n")
cols <- c(1, 2, 4, 5)
print.fdt_cat.default(tdf_categorias, columns = cols, round = 2, 
                      row.names = FALSE, right = FALSE)

# Exemplo de vetor categórico com números e texto
categorias2 <- c(
  "A", "B", "C", 1, 2, 3, "A", 1, "C", "B",
  2, "A", "C", 3, "B", 1, "C", "A", 2, 3,
  "B", 1, "C", 2, "A", "B", 3, "C", 1, 2
)

tdf_categorias2 <- fdt_cat.default(categorias2)
cat("\nTDF Categorica 2\n\n")

print.fdt_cat.default(x = tdf_categorias2, round=2)