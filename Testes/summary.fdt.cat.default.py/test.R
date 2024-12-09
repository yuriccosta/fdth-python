library(fdth)

# Teste 1: Simples com frequências e percentuais
x1 <- data.frame(
  Category = c("A", "B", "C"),
  f = c(10, 20, 30),
  rf = c(0.1, 0.2, 0.3),
  `rf(%)` = c(10.0, 20.0, 30.0),
  cf = c(10, 30, 60),
  `cf(%)` = c(10.0, 30.0, 60.0)
)

cat("Teste 1: Simples com frequências e percentuais\n")
resultado3 <- print.fdt_cat.default(x1, columns=1:6, round=2)
print(resultado3)
print(x1)
# Teste 2: Dados com números decimais
x2 <- data.frame(
  Category = c("D", "E", "F"),
  f = c(5.5, 7.25, 12.75),
  rf = c(0.15, 0.25, 0.6),
  `rf(%)` = c(15.0, 25.0, 60.0),
  cf = c(5.5, 12.75, 25.5),
  `cf(%)` = c(15.0, 40.0, 100.0)
)

cat("\nTeste 2: Dados com números decimais\n")
print.fdt_cat.default(x2, columns=1:6, round=2)

# Teste 3: Usando menos colunas (apenas Category, f e rf(%))
x3 <- data.frame(
  Category = c("G", "H", "I"),
  f = c(8, 12, 10),
  `rf(%)` = c(16.0, 24.0, 20.0)
)

cat("\nTeste 3: Usando menos colunas (Category, f, rf(%))\n")
print.fdt_cat.default(x3, columns=1:3, round=2)
