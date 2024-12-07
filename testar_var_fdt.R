# Teste para a função var_fdt em R
library(testthat)

testar_var_fdt <- function() {
  cat("Testando var_fdt...\n")
  
  # Teste 1 - Caso base
  x_test1 <- list(
    breaks = list(start = 0, end = 40, h = 10),
    table = matrix(c(1, 5, 2, 10, 3, 15, 4, 10), ncol = 2, byrow = TRUE)
  )
  resultado1 <- var_fdt(x_test1)
  esperado1 <- 96.15
  cat("Resultado obtido:", resultado1, "\n")
  cat("Esperado:", esperado1, "\n")
  expect_equal(round(resultado1, 2), round(esperado1, 2), tolerance = 0.01)

  # Teste 2 - Menor tabela e intervalo diferente
  x_test2 <- list(
    breaks = list(start = 0, end = 20, h = 5),
    table = matrix(c(1, 8, 2, 12, 3, 10, 4, 5), ncol = 2, byrow = TRUE)
  )
  resultado2 <- var_fdt(x_test2)
  esperado2 <- 66.67  # Valor fictício, substituir pelo correto
  cat("Resultado obtido:", resultado2, "\n")
  cat("Esperado:", esperado2, "\n")
  expect_equal(round(resultado2, 2), round(esperado2, 2), tolerance = 0.01)

  # Teste 3 - Tabela com valores uniformes
  x_test3 <- list(
    breaks = list(start = 10, end = 50, h = 10),
    table = matrix(c(1, 10, 2, 10, 3, 10, 4, 10), ncol = 2, byrow = TRUE)
  )
  resultado3 <- var_fdt(x_test3)
  esperado3 <- 0.0  # Variância de dados uniformes é zero
  cat("Resultado obtido:", resultado3, "\n")
  cat("Esperado:", esperado3, "\n")
  expect_equal(round(resultado3, 2), round(esperado3, 2), tolerance = 0.01)

  # Teste 4 - Tabela com valores maiores
  x_test4 <- list(
    breaks = list(start = 0, end = 100, h = 20),
    table = matrix(c(1, 20, 2, 30, 3, 25, 4, 25), ncol = 2, byrow = TRUE)
  )
  resultado4 <- var_fdt(x_test4)
  esperado4 <- 225.0  # Valor fictício, substituir pelo correto
  cat("Resultado obtido:", resultado4, "\n")
  cat("Esperado:", esperado4, "\n")
  expect_equal(round(resultado4, 2), round(esperado4, 2), tolerance = 0.01)
}

# Executa os testes
testar_var_fdt()
