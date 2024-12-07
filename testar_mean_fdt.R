
# Teste para a função mean_fdt em R

testar_mean_fdt <- function() {
  cat("Testando mean_fdt...\n")

  # Teste 1 - Caso base
  x_test1 <- list(
    breaks = list(start = 0, end = 40, h = 10),
    table = matrix(c(1, 5, 2, 10, 3, 15, 4, 10), ncol = 2, byrow = TRUE)
  )
  resultado1 <- mean_fdt(x_test1)
  esperado1 <- 22.5
  cat("Resultado obtido: ", resultado1, "\n")
  cat("Esperado: ", esperado1, "\n")
  stopifnot(abs(resultado1 - esperado1) < 1e-9)

  # Teste 2 - Intervalos menores e distribuição uniforme
  x_test2 <- list(
    breaks = list(start = 0, end = 20, h = 5),
    table = matrix(c(1, 10, 2, 10, 3, 10, 4, 10), ncol = 2, byrow = TRUE)
  )
  resultado2 <- mean_fdt(x_test2)
  esperado2 <- 10.0
  cat("Resultado obtido: ", resultado2, "\n")
  cat("Esperado: ", esperado2, "\n")
  stopifnot(abs(resultado2 - esperado2) < 1e-9)

  # Teste 3 - Intervalos maiores e pesos variados
  x_test3 <- list(
    breaks = list(start = 0, end = 100, h = 20),
    table = matrix(c(1, 5, 2, 15, 3, 10, 4, 20, 5, 10), ncol = 2, byrow = TRUE)
  )
  resultado3 <- mean_fdt(x_test3)
  esperado3 <- 50.0
  cat("Resultado obtido: ", resultado3, "\n")
  cat("Esperado: ", esperado3, "\n")
  stopifnot(abs(resultado3 - esperado3) < 1e-9)

  # Teste 4 - Tabela com valores decrescentes
  x_test4 <- list(
    breaks = list(start = 0, end = 50, h = 10),
    table = matrix(c(1, 20, 2, 15, 3, 10, 4, 5), ncol = 2, byrow = TRUE)
  )
  resultado4 <- mean_fdt(x_test4)
  esperado4 <- 17.5
  cat("Resultado obtido: ", resultado4, "\n")
  cat("Esperado: ", esperado4, "\n")
  stopifnot(abs(resultado4 - esperado4) < 1e-9)
}

# Executando os testes
testar_mean_fdt()
