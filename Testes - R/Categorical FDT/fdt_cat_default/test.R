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

# Teste 1 em R
#x <- c("A", "B", "A", "C", "B", "A", "C", "C", "A", "B")
#res_r <- fdt_cat.default(x, sort=TRUE, decreasing=TRUE)
#print(res_r)

# Teste 2 em R
#x <- c("X", "X", "X", "X", "X", "X")
#res_r <- fdt_cat.default(x, sort=FALSE, decreasing=FALSE)
#print(res_r)

# Teste 3 em R
x <- c("Dog", "Cat", "Cat", "Dog", "Fish", "Fish", "Bird", "Dog")
res_r <- fdt_cat.default(x, sort=TRUE, decreasing=FALSE)
print(res_r)
