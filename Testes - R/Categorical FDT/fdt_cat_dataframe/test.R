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

make.fdt_cat.multiple <- function(x,
                                  sort,
                                  decreasing)
{
  stopifnot(is.data.frame(x))

  res <- list()

  f <- sapply(x, 
              is.factor)

  for(i in 1:ncol(x)){
    if(f[i]){
      m  <- x[,i]

      fdt <- make.fdt_cat.simple(m,
                                 sort,
                                 decreasing)
      res <- c(res,
               list(fdt))
    }
  }
  valCol <- f[f]

  names(res) <- names(valCol)

  return(res)  
}

fdt_cat.data.frame <- function (x,
                                by,
                                sort=TRUE,
                                decreasing=TRUE, ...)
{
 stopifnot(is.data.frame(x))

 res <- list()

 # User do not defines a factor
 if (missing(by)) {

  #x <- na.omit(x)

  logCol <- sapply(x,
                   is.factor)

  for (i in 1:ncol(x)) {
   if (logCol[i]) {
    m <- as.data.frame(x[, i])

    fdt <- make.fdt_cat.multiple(m,
                                 sort,
                                 decreasing)

    tmpres <- list(table=fdt[[1]])

    res <- c(res,
             list(tmpres))
   }
  }

  valCol     <- logCol[logCol]

  names(res) <- names(valCol) 
 }

 # User defines one factor
 else {

  nameF   <- character()
  nameY   <- character()
  namesdf <- names(x)
  pos     <- which(namesdf == by)

  stopifnot(is.factor((x[[pos]])))

  numF <- table(x[[pos]])
  for (i in 1:length(numF)) {
   tmpdf  <- subset(x,
                    x[[pos]] == names(numF[i]))
   tmpdf <- tmpdf[-pos]
   logCol <- sapply(tmpdf,
                    is.factor)

   for (j in 1:ncol(tmpdf)) {
    if (logCol[j]) {
     m <- as.data.frame(tmpdf[, j])

     fdt <- make.fdt_cat.multiple(m,
                                  sort,
                                  decreasing)
     newFY  <- list(fdt)
     nameF  <- names(numF[i])
     nameY  <- names(logCol[j])
     nameFY <- paste(nameF,
                     '.',
                     nameY,
                     sep="")

     names(newFY) <- sub(' +$',
                         '',
                         nameFY)
     res <- c(res,
              newFY)
    }
   }
  }
 }

 class(res) <- c('fdt_cat.multiple',
                 'fdt_cat',
                 'list')

 invisible(res)
}

# Carregar as funções make.fdt_cat.multiple e fdt_cat.data.frame antes de executar os testes

# Teste 1: Sem agrupamento
df1 <- data.frame(
  col1 = factor(c('A', 'B', 'A', 'C', 'C')),
  col2 = factor(c('X', 'X', 'Y', 'X', 'Y'))
)
result1 <- fdt_cat.data.frame(df1, sort = TRUE, decreasing = TRUE)
print(result1)

# Teste 2: Com agrupamento
#df2 <- data.frame(
#  group = factor(c('G1', 'G1', 'G2', 'G2', 'G2')),
#  col1 = factor(c('A', 'B', 'A', 'C', 'C')),
#  col2 = factor(c('X', 'X', 'Y', 'X', 'Y'))
#)
#result2 <- fdt_cat.data.frame(df2, by = "group", sort = TRUE, decreasing = FALSE)
#print(result2)

# Teste 3: Com coluna numérica
#df3 <- data.frame(
#  col1 = factor(c('A', 'B', 'A', 'C', 'C')),
#  col2 = factor(c('X', 'X', 'Y', 'X', 'Y')),
#  col3 = c(1, 2, 3, 4, 5)  # Coluna numérica
#)
#result3 <- fdt_cat.data.frame(df3, sort = FALSE)
#print(result3)
