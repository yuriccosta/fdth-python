fdt.default <- function (x,
                         k,
                         start,
                         end,
                         h,
                         breaks=c('Sturges', 'Scott', 'FD'),
                         right=FALSE,
                         na.rm=FALSE, ...)
{
  # User defines nothing or not 'x' isn't numeric -> stop
  stopifnot(is.numeric(x))

  #x <- na.omit(x)

  # User defines only 'x'
  if (missing(k) && 
      missing(start) && 
      missing(end) && 
      missing(h)) {

    brk <- match.arg(breaks)

    switch (brk,
            Sturges = (k <- nclass.Sturges(x)),
            Scott   = (k <- nclass.scott(x)),
            FD      = (k <- nclass.FD(x)))

    if (any(is.na(x)) & na.rm == FALSE)
      stop('The data has <NA> values and na.rm=FALSE by default.')

    tmp   <- range(x,
                   na.rm=na.rm)
    start <- tmp[1] - abs(tmp[1])/100
    end   <- tmp[2] + abs(tmp[2])/100
    R     <- end - start
    h     <- R/k
  }

  # User defines 'x' and 'k'
  else if (missing(start) && 
           missing(end) && 
           missing(h)) {
    stopifnot(length(k) >= 1)

    if (any(is.na(x)) & na.rm == FALSE)
      stop('The data has <NA> values and na.rm=FALSE by default.')

    tmp   <- range(x,
                   na.rm=na.rm)
    start <- tmp[1] - abs(tmp[1])/100
    end   <- tmp[2] + abs(tmp[2])/100
    R     <- end - start
    h     <- R/abs(k)
  }

  # User defines 'x', 'start' and 'end'
  else if (missing(k) && 
           missing(h)) {
    stopifnot(length(start) >= 1,
              length(end) >=1)
    R   <- end - start
    k   <- sqrt(abs(R))
    if (k < 5) k = 5 # min value of k
    h   <- R/k
  }

  # User defines 'x', 'start', 'end' and 'h'
  else if (missing(k)) {
    stopifnot(length(start) >= 1,
              length(end) >= 1,
              length(h) >= 1)
  }

  else stop('Please, see the function sintaxe!')

  fdt <- make.fdt.simple(x,
                         start,
                         end,
                         h,
                         right)

  breaks <- c(start,
              end,
              h,
              ifelse (right,
                      1,
                      0))

  names(breaks) <- c('start',
                     'end',
                     'h',
                     'right')

  res <- list(table=fdt,
              breaks=breaks)

  class(res) <- c('fdt.default',
                  'fdt',
                  'list')

  invisible(res)
} 

make.fdt.simple <- function (x,
                             start,
                             end,
                             h,
                             right)

{
  ## Ivan B. Allaman: thank you to the bug fix
  f <- table(cut(x,
                 br=seq(start,
                        end,
                        h),
                 right=right,
                 dig.lab=nchar(as.character(round(max(end),
                                                  2)))))    # Absolute freq.
  rf  <- as.numeric(f/length(x))                            # Relative freq
  rfp <- as.numeric(100*(f/length(x)))                      # Relative freq, %
  cf  <- as.numeric(cumsum(f))                              # Cumulative freq
  cfp <- as.numeric(100*(cumsum(f/length(x))))              # Cumulative freq, %

  res <- data.frame(f,                                      # Make final table
                    rf,
                    rfp,
                    cf,
                    cfp)                   

  names(res) <- c('Class limits',
                  'f',
                  'rf',
                  'rf(%)',
                  'cf', 
                  'cf(%)')

  return(res)
}

fdt <- function(x, ...) UseMethod('fdt')

median.fdt <- function(x, ...)
{
  fdt <- with(x,
              table)

  n <- fdt[nrow(fdt), 5]

  posM <- grep(TRUE,
               n / 2 <= fdt[, 5])[1]

  brk <- with(x,
              seq(breaks['start'],
                  breaks['end'],
                  breaks['h']))

  liM <- brk[posM]

  # It is important if 'posM' is inside of the first class
  if (posM - 1 <= 0)
    sfaM <- 0
  else
    sfaM <- fdt[(posM - 1), 5]

  fM <- fdt[posM, 2]

  h <- as.vector(with(x,
                      breaks['h']))

  res <- liM + (((n / 2) - sfaM) * h) / fM

  return(res)
}                        

# Dados de exemplo
dados <- c(10, 12, 15, 20, 22, 25, 25, 30, 35, 40)

# Criar uma tabela de frequências agrupada (fdt)
tabela_fdt <- fdt(dados)

# Visualizar o resultado
print(tabela_fdt$table)
mediana <- median.fdt(tabela_fdt)
cat("A mediana é: ", mediana)
cat("\n")

