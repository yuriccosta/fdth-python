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
fdt.data.frame <- function (x,
                            k,
                            by,
                            breaks=c('Sturges', 'Scott', 'FD'),
                            right=FALSE,
                            na.rm=FALSE, ...)
{
  stopifnot(is.data.frame(x))

  rec <- match.call(expand.dots = TRUE)
  res <- list()

  # User do not defines a factor
  if (missing(by)) {
    logCol <- sapply(x,
                     is.numeric)

    for (i in 1:ncol(x)) {
      if (logCol[i]) {
        m <- as.matrix(x[, i])

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

      logCol <- sapply(tmpdf,
                       is.numeric)

      for (j in 1:ncol(tmpdf)) {
        if (logCol[j]) {
          m <- as.matrix(tmpdf[, j])

          fdt <- make.fdt.multiple(m,
                                   k,
                                   breaks,
                                   right,
                                   na.rm)
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
  res$call <- rec
  class(res) <- c('fdt.multiple',
                  'fdt',
                  'list')
  invisible(res)
} 

# Teste 1
df1 <- data.frame(A = c(1, 2, 2, 3, 3, 3, 4, 4, 4, 4))
result1 <- fdt.data.frame(df1)
cat("Table:\n")
print(result1$A$table)
cat("\nBreaks:\n")
print(result1$A$breaks)

# Teste 2
#df2 <- data.frame(
#  A = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
#  B = c(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
#)
#result2 <- fdt.data.frame(df2)
#print(result2)

# Teste 3
#df3 <- data.frame(
#  A = c(1, 2, 2, 3, 3, 3, 4, 4, 4, 4),
#  B = c(10, 20, 20, 30, 30, 30, 40, 40, 40, 40),
#  Group = factor(c("G1", "G1", "G1", "G1", "G2", "G2", "G2", "G2", "G2", "G2"))
#)
#result3 <- fdt.data.frame(df3, by = "Group")
#print(result3)

