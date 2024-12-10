make.fdt_cat.simple <- function(x,
                                sort,
                                decreasing)
{
  stopifnot(is.character(x) |
            is.factor(x))

  x <- as.factor(x)

  f <- as.vector(table(x))

  if (sort) {
    order.f <- order(f,
                     decreasing=decreasing)

    f <- f[order.f]

    category <- levels(x)[order.f]
  } else {
    category <- levels(x)
  }

  rf  <- f / sum(f)             # Relative freq
  rfp <- rf * 100               # Relative freq, %
  cf  <- cumsum(f)              # Cumulative freq
  cfp <- cumsum(rfp)            # Cumulative freq, %

  res <- data.frame(category,   # Make final table
                    f,
                    rf,
                    rfp,
                    cf,
                    cfp)

  names(res) <- c('Category',
                  'f',
                  'rf',
                  'rf(%)',
                  'cf',
                  'cf(%)')

  return(res)
}
fdt_cat.default <- function (x,
                             sort=TRUE,
                             decreasing=TRUE, ...)
{
  #x <- na.omit(x)

  res <- make.fdt_cat.simple(x,
                             sort,
                             decreasing)

  class(res) <- c('fdt_cat.default',
                  'fdt_cat',
                  'data.frame')

  invisible(res)
}  

fdt_cat <-
  function (x, ...) UseMethod('fdt_cat')

summary.fdt_cat.default <- function (object,
                                     columns=1:6,
                                     round=2,
                                     row.names=FALSE,
                                     right=TRUE, ...)
{
  res <- cbind(object[, 1],
               round(object[, 2:6],
                     round))[columns]

  names(res) <- c('Category',
                  'f',
                  'rf',
                  'rf(%)',
                  'cf',
                  'cf(%)')[columns]

  res <- print.data.frame(res,
                          row.names=row.names,
                          right=right, ...)
}

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
summary.fdt_cat.default(tdf_categorias, columns = cols, round = 2, 
                      row.names = FALSE, right = FALSE)

# Exemplo de vetor categórico com números e texto
categorias2 <- c(
  "A", "B", "C", 1, 2, 3, "A", 1, "C", "B",
  2, "A", "C", 3, "B", 1, "C", "A", 2, 3,
  "B", 1, "C", 2, "A", "B", 3, "C", 1, 2
)

tdf_categorias2 <- fdt_cat.default(categorias2)
cat("\nTDF Categorica 2\n\n")

summary.fdt_cat.default(object = tdf_categorias2, round=2)