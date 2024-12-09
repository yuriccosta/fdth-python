library(fdth)
# Redireciona as saídas do console temporariamente
suppressMessages({
  suppressWarnings({
    library(fdth)
  })
})


# Dados de exemplo
dados <- c(10, 12, 15, 20, 22, 25, 25, 30, 35, 40)

# Criar uma tabela de frequências agrupada (fdt)
tabela_fdt <- fdt(dados)

# Visualizar o resultado
print(tabela_fdt)
median.fdt(tabela_fdt)

