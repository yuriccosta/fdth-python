mfv.default <- function(x, ...)
{
  # Adapted from
  # http://stackoverflow.com/questions/2547402/standard-library-function-in-r-for-finding-the-mode
  ux <- unique(x)

  res <- as.vector(ux[which.max(tabulate(match(x, 
                                               ux)))])
  return(res)
}                        

data1 <- c(1, 2, 2, 3, 4)
cat("A moda de data1 é:", mfv.default(data1), "\n")

# Conjunto de dados com múltiplas modas
data2 <- c(1, 1, 2, 2, 3)
cat("A moda de data2 é:", mfv.default(data2), "\n")

# Conjunto de dados onde todos os valores são únicos
data3 <- c(1, 2, 3, 4, 5)
cat("A moda de data3 é:", mfv.default(data3), "\n")

# Conjunto de dados onde todos os valores são iguais
data4 <- c(2, 2, 2, 2, 2)
cat("A moda de data4 é:", mfv.default(data4), "\n")

# Conjunto de dados vazio
data5 <- c()
cat("A moda de data5 é:", mfv.default(data5), "\n")

# Conjunto de dados com valores não numéricos
data6 <- c('a', 'b', 'b', 'c')
cat("A moda de data6 é:", mfv.default(data6), "\n")
