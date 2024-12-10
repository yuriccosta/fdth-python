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

# Dados para os testes
x_test1 <- list(
  breaks = list(start = 0, end = 10, h = 2),
  table = matrix(c(0, 2, 2, 2, 4, 2, 6, 2, 8, 2), ncol = 2, byrow = TRUE)
)

x_test2 <- list(
  breaks = list(start = 0, end = 12, h = 3),
  table = matrix(c(0, 1, 3, 2, 6, 3, 9, 4), ncol = 2, byrow = TRUE)
)

x_test3 <- list(
  breaks = list(start = 0, end = 16, h = 4),
  table = matrix(c(0, 8, 4, 6, 8, 4, 12, 2), ncol = 2, byrow = TRUE)
)

x_test4 <- list(
  breaks = list(start = 0, end = 20, h = 5),
  table = matrix(c(0, 3, 5, 7, 10, 5, 15, 2), ncol = 2, byrow = TRUE)
)

# Executando os testes
cat("Teste 1 (Desvio Padrão):", sd_fdt(x_test1), "\n")
cat("Teste 2 (Desvio Padrão):", sd_fdt(x_test2), "\n")
cat("Teste 3 (Desvio Padrão):", sd_fdt(x_test3), "\n")
cat("Teste 4 (Desvio Padrão):", sd_fdt(x_test4), "\n")