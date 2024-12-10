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

# Carregar a função fdt.default e make.fdt.simple antes de executar os testes.

# Teste 1
dados <- c(2, 5, 7, 10, 12, 15, 18)
resultado <- fdt.default(dados, breaks = 'Sturges')
print(resultado$table)

# Teste 2
#dados <- c(3, 6, 9, 12, 15, 18, 21)
#resultado <- fdt.default(dados, k = 4)
#print(resultado$table)

# Teste 3
#dados <- c(1, 4, 7, 10, 13, 16, 19)
#resultado <- fdt.default(dados, start = 0, end = 20)
#print(resultado$table)

# Teste 4
#dados <- c(10, 15, 20, 25, 30, 35, 40)
#resultado <- fdt.default(dados, start = 10, end = 50, h = 8)
#print(resultado$table)

# Teste 5
#tryCatch({
#   dados <- c(2, NA, 8, 10, NA, 18)
#   resultado <- fdt.default(dados, na.rm = FALSE)
# }, error = function(e) {
#   cat("Erro:", e$message, "\n")
# })

# Teste 6
# tryCatch({
#   dados <- c(1, 2, 3, 4)
#  resultado <- fdt.default(dados, start = 1, end = 5, k = 2, h = 1)
# }, error = function(e) {
#   cat("Erro:", e$message, "\n")
# })


