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

fdt_cat.matrix <- function (x,
                            sort=TRUE,
                            decreasing=TRUE, ...)
{
  stopifnot(is.matrix(x))

  res <- list()

  #x <- na.omit(x)
 
  for (i in 1:ncol(x)) {
    m <- as.matrix(x[ ,i])

    fdt <- make.fdt_cat.simple(m,
                               sort,
                               decreasing)
    
    tmpres <- list(table=list(fdt)[[1]]) 

    res <- c(res,
             list(tmpres))
  }

  if (is.null(colnames(x)))
    nms <- paste('Column',
                 1:ncol(x),
                 sep=':')
  else
    nms <- colnames(x)

  names(res) <- nms

  class(res) <- c('fdt_cat.multiple',
                  'fdt_cat',
                  'list')

  invisible(res)
}

# Carregar a função fdt_cat.matrix e make.fdt_cat.simple antes de executar os testes

# Teste 1
#x <- matrix(
#  c("A", "B", "C",
#   "A", "B", "C",
#    "B", "A", "C",
#    "C", "A", "B"),
#  nrow = 4,
#  byrow = TRUE
#)
#colnames(x) <- c("Col1", "Col2", "Col3")
#res <- fdt_cat.matrix(x, sort = TRUE, decreasing = TRUE)
#print(res)

# Teste 2
#x <- matrix(
#  c("X", "Y", "Z",
#    "X", "Y", "Z",
#    "X", "Y", "Z",
#    "X", "Y", "Z"),
#  nrow = 4,
#  byrow = TRUE
#)
#colnames(x) <- c("Col1", "Col2", "Col3")
#res <- fdt_cat.matrix(x, sort = TRUE, decreasing = TRUE)
#print(res)

# Teste 3
x <- matrix(
  c("Dog", "Cat", "Fish",
    "Dog", "Dog", "Bird",
    "Cat", "Cat", "Fish",
    "Fish", "Dog", "Bird"),
  nrow = 4,
  byrow = TRUE
)
colnames(x) <- c("Col1", "Col2", "Col3")
res <- fdt_cat.matrix(x, sort = TRUE, decreasing = FALSE)
print(res)


