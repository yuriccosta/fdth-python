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

summary.fdt.default <- function (object,
                                 columns=1:6,
                                 round=2, 
                                 format.classes=FALSE,
                                 pattern='%09.3e',
                                 row.names=FALSE,
                                 right=TRUE, ...)
{
  res <- object[['table']]

  res <- cbind(res[, 1], 
               round(res[, 2:6],
                     round))[columns]

  right.tmp <- as.logical(object[['breaks']]['right'])

  if (format.classes) {
    tmp <- as.character(res[, 1])
    res[, 1] <- make.fdt.format.classes(tmp, 
                                        right.tmp, 
                                        pattern)
  }

  names(res) <- c('Class limits',
                  'f',
                  'rf',
                  'rf(%)',
                  'cf',
                  'cf(%)')[columns]

  res <- print.data.frame(res,
                          row.names=row.names,
                          right=right, ...)
}

make.fdt.format.classes <- function (x,
                                     right,
                                     pattern)
{
  tmp <- strsplit(x,
                  ',')

  res <- lapply(tmp,
                function (.vals) {
                  .vals[1L] <- sprintf(ifelse(right,
                                              paste('(',
                                                    pattern,
                                                    sep=''),
                                              paste('[', 
                                                    pattern,
                                                    sep='')),
                                       as.numeric(substring(.vals[1L], 2)))
                  .vals[2L] <- sprintf(ifelse (right,
                                               paste(pattern,
                                                     ']',
                                                     sep=''),
                                               paste(pattern,
                                                     ')',
                                                     sep='')),
                                       as.numeric(substring(.vals[2L], 1,
                                                            nchar(.vals[2L]) - 1)))
                  paste(.vals, 
                        collapse=', ')
                })

  invisible(unlist(res))
}


# Gera um vetor de números aleatórios normais, com média 5 e desvio padrão 2
# x <- rnorm(100, mean = 5, sd = 2)

x <- c(6.34, 4.57, 7.89, 5.12, 4.26, 5.77, 2.95, 8.13, 3.48, 6.05, 
       4.93, 6.88, 7.21, 3.69, 5.55, 2.87, 5.02, 4.31, 6.79, 3.98, 
       7.44, 5.36, 6.12, 4.59, 8.27, 3.65, 5.48, 7.81, 3.93, 5.67)

# gera a tabela de distribuição de frequências
x <- fdt.default(x, breaks = "Sturges")

# Formata a tabela com a summary
cat("Exemplo com seleção de colunas e nome de colunas\n")
X1 <- summary.fdt.default(x, columns = 1:3, round = 2, row.names = TRUE)

cat("\nExemplo com seleção de colunas e formatação de classes\n")
col <- c(1, 4, 6)
X2 <- summary.fdt.default(x, columns = col, format.classes = TRUE, pattern = "%.5e")
