# Função para calcular a média ponderada
mean_fdt <- function(x) {
  breaks <- seq(x$breaks$start, x$breaks$end, by = x$breaks$h)
  mids <- (breaks[-length(breaks)] + breaks[-1]) / 2
  y <- x$table[, 2]
  mean <- sum(y * mids) / sum(y)
  return(mean)
}

# Função para calcular a variância ponderada
var_fdt <- function(x) {
  breaks <- seq(x$breaks$start, x$breaks$end, by = x$breaks$h)
  mids <- (breaks[-length(breaks)] + breaks[-1]) / 2
  y <- x$table[, 2]
  mean <- mean_fdt(x)
  var <- sum(y * (mids - mean)^2) / (sum(y) - 1)
  return(var)
}

# Função para calcular o desvio padrão ponderado
sd_fdt <- function(x) {
  var <- var_fdt(x)
  sd <- sqrt(var)
  return(sd)
}

# Teste para a função sd_fdt
testar_sd_fdt <- function() {
  x_test <- list(
    breaks = list(start = 0, end = 40, h = 10),
    table = matrix(c(1, 5, 2, 10, 3, 15, 4, 10), ncol = 2, byrow = TRUE)
  )

  resultado <- sd_fdt(x_test)
  esperado <- 9.8
  cat("Resultado sd_fdt:", resultado, "\n")
  stopifnot(abs(resultado - esperado) < 0.01)
}

# Executar o teste
testar_sd_fdt()



# Testando a função sd_fdt
testar_sd_fdt <- function() {
  cat("Testando sd_fdt...\n")
  
  # Teste 1: Caso básico
  x_test_1 <- list(
    breaks = list(start = 0, end = 40, n = 4),
    table = matrix(c(1, 5, 2, 10, 3, 15, 4, 10), ncol = 2, byrow = TRUE)
  )
  resultado_1 <- sd_fdt(x_test_1)
  esperado_1 <- 9.8
  cat(sprintf("Teste 1 - Resultado obtido: %f, Esperado: %f\n", resultado_1, esperado_1))
  stopifnot(abs(resultado_1 - esperado_1) < 0.01)

  # Teste 2: Frequências mais altas
  x_test_2 <- list(
    breaks = list(start = 0, end = 50, n = 5),
    table = matrix(c(1, 10, 2, 20, 3, 30, 4, 25, 5, 15), ncol = 2, byrow = TRUE)
  )
  resultado_2 <- sd_fdt(x_test_2)
  esperado_2 <- 12.03
  cat(sprintf("Teste 2 - Resultado obtido: %f, Esperado: %f\n", resultado_2, esperado_2))
  stopifnot(abs(resultado_2 - esperado_2) < 0.01)

  # Teste 3: Distribuição uniforme
  x_test_3 <- list(
    breaks = list(start = 0, end = 100, n = 5),
    table = matrix(c(1, 20, 2, 20, 3, 20, 4, 20, 5, 20), ncol = 2, byrow = TRUE)
  )
  resultado_3 <- sd_fdt(x_test_3)
  esperado_3 <- 28.72
  cat(sprintf("Teste 3 - Resultado obtido: %f, Esperado: %f\n", resultado_3, esperado_3))
  stopifnot(abs(resultado_3 - esperado_3) < 0.01)

  # Teste 4: Frequência única (caso limite)
  x_test_4 <- list(
    breaks = list(start = 0, end = 10, n = 1),
    table = matrix(c(1, 100), ncol = 2, byrow = TRUE)
  )
  resultado_4 <- sd_fdt(x_test_4)
  esperado_4 <- 0.0
  cat(sprintf("Teste 4 - Resultado obtido: %f, Esperado: %f\n", resultado_4, esperado_4))
  stopifnot(abs(resultado_4 - esperado_4) < 0.01)
}

# Executando os testes
testar_sd_fdt()
