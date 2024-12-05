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
