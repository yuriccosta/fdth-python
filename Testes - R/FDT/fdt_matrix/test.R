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
make.fdt.multiple <- function (x,
                               k,
                               breaks=c('Sturges', 'Scott', 'FD'),
                               right,
                               na.rm)
{
  #x <- na.omit(x)

  # Built-in functions adapted from grDevices package to accept 'na.rm' argument
  nclass.Scott_local <-
  function (x,
            na.rm=FALSE)
  {
      h <- 3.5 * sqrt(stats::var(x,
                                 na.rm=na.rm)) * length(x)^(-1/3)
      if (h > 0)
          max(1, ceiling(diff(range(x,
                                    na.rm=na.rm))/h))
      else 1L
  }


  nclass.FD_local <-
  function (x,
            na.rm=FALSE)
  {
      h <- 2 * stats::IQR(x. <- signif(x,
                                       digits = 5),
                          na.rm=na.rm)
      if (h == 0) {
          x. <- sort(x.)
          al <- 1/4
          al.min <- 1/512
          while (h == 0 && (al <- al/2) >= al.min)
            h <- diff(stats::quantile(x.,
                                      c(al, 1 - al),
                                      names = FALSE,
                                      na.rm=na.rm))/(1 - 2 * al)
      }
      if (h == 0)
          h <- 3.5 * sqrt(stats::var(x,
                                     na.rm=na.rm))
      if (h > 0)
          ceiling(diff(range(x,
                             na.rm=na.rm))/h * length(x)^(1/3))
      else 1L
  }

  # User defines only x and/or 'breaks'
  if (missing(k)) {
    brk <- match.arg(breaks)

    switch (brk,
            Sturges = (k <- nclass.Sturges(x)),

            Scott   = if (any(is.na(x)) & na.rm == FALSE)
                        stop('The data has <NA> values and na.rm=FALSE by default.')
                      else
                        (k <- nclass.Scott_local(x,
                                                 na.rm=na.rm)),

            FD      = if (any(is.na(x)) & na.rm == FALSE)
                        stop('The data has <NA> values and na.rm=FALSE by default.')
                      else
                        (k <- nclass.FD_local(x,
                                              na.rm=na.rm)))

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
  else {
    if (any(is.na(x)) & na.rm == FALSE)
      stop('The data has <NA> values and na.rm=FALSE by default.')

    tmp   <- range(x,
                   na.rm=na.rm)
    start <- tmp[1] - abs(tmp[1])/100
    end   <- tmp[2] + abs(tmp[2])/100
    R     <- end - start
    h     <- R/abs(k)
  }

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

  return (res)
}
fdt.matrix <- function (x,
                        k,
                        breaks=c('Sturges', 'Scott', 'FD'),
                        right=FALSE,
                        na.rm=FALSE, ...)
{
  stopifnot(is.matrix(x))

  res <- list()

  for (i in 1:ncol(x)) {
    m <- as.matrix(x[ ,i])

    fdt <- make.fdt.multiple(m,
                             k,
                             breaks,
                             right,
                             na.rm)

    tmpres <- list(table=fdt[[1]],
                   breaks=fdt[[2]])

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

  class(res) <- c('fdt.multiple',
                  'fdt',
                  'list')

  invisible(res)
} 

# Criar a matriz de dados para os testes
data_matrix <- matrix(c(1, 2, 3, 4, 5, 10, 20, 30, 40, 50), ncol = 2)

# Teste 1: Especificando k = 3
result_k3 <- fdt.matrix(data_matrix, k = 3, right = FALSE, na.rm = FALSE)
print(result_k3)

# Teste 2: Com breaks = 'Sturges'
#result_sturges <- fdt.matrix(data_matrix, breaks = "Sturges", right = FALSE, na.rm = FALSE)
#print(result_sturges)

# Teste 3: Com breaks = 'Scott'
#result_scott <- fdt.matrix(data_matrix, breaks = "Scott", right = FALSE, na.rm = FALSE)
#print(result_scott)

# Teste 4: Com breaks = 'FD'
#result_fd <- fdt.matrix(data_matrix, breaks = "FD", right = FALSE, na.rm = FALSE)
#print(result_fd)

# Teste 5: Com right = TRUE
#result_right <- fdt.matrix(data_matrix, k = 3, right = TRUE, na.rm = FALSE)
#print(result_right)

