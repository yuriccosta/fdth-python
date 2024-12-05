# Função para calcular a média ponderada
mean_fdt <- function(x) {
  breaks <- seq(x$breaks$start, x$breaks$end, by = x$breaks$h)
  mids <- (breaks[-length(breaks)] + breaks[-1]) / 2
  y <- x$table[, 2]
  mean <- sum(y * mids) / sum(y)
  return(mean)
}

# Teste para a função mean_fdt
testar_mean_fdt <- function() {
  x_test <- list(
    breaks = list(start = 0, end = 40, h = 10),
    table = matrix(c(1, 5, 2, 10, 3, 15, 4, 10), ncol = 2, byrow = TRUE)
  )

  resultado <- mean_fdt(x_test)
  esperado <- 22.5
  cat("Resultado mean_fdt:", resultado, "\n")
  stopifnot(abs(resultado - esperado) < 1e-6)
}

# Executar o teste
testar_mean_fdt()
