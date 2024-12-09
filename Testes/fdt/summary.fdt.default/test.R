library(fdth)

# Gera um vetor de números aleatórios normais, com média 5 e desvio padrão 2
# x <- rnorm(100, mean = 5, sd = 2)

x <- c(6.34, 4.57, 7.89, 5.12, 4.26, 5.77, 2.95, 8.13, 3.48, 6.05, 
       4.93, 6.88, 7.21, 3.69, 5.55, 2.87, 5.02, 4.31, 6.79, 3.98, 
       7.44, 5.36, 6.12, 4.59, 8.27, 3.65, 5.48, 7.81, 3.93, 5.67)

# gera a tabela de distribuição de frequências
x <- fdt.default(x, breaks = "Sturges")

# Formata a tabela com a summary
cat("\nExemplo com seleção de colunas e nome de colunas\n")
X1 <- summary.fdt.default(x, columns = 1:3, round = 2, row.names = TRUE)

cat("\nExemplo com seleção de colunas e formatação de classes\n")
col <- c(1, 4, 6)
X2 <- summary.fdt.default(x, columns = col, format.classes = TRUE, pattern = "%.5e")
