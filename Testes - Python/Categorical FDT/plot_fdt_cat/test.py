import pandas as pd
from fdt_cat_data_frame import fdt_cat_data_frame  # Supondo que este módulo já está implementado.
from plot_fdt_cat_default import plot_fdt_cat  # Supondo que este módulo já está implementado.

# Dados de exemplo corrigidos
data = {
    "Category": ["Segurança"] * 18 + 
               ["Trânsito"] * 17 + 
               ["Trans. Público"] * 16 + 
               ["Saúde"] * 7 + 
               ["Educação"] * 5 + 
               ["Outros"] * 3
}

df = pd.DataFrame(data)

# Gerar a tabela de frequência utilizando o método fdt_cat_data_frame
fdt_result = fdt_cat_data_frame(df, sort=True, decreasing=True)

# Obter o primeiro resultado do FDTResultMultiple
fdt_df = list(fdt_result.results.values())[0]

# Plotar o gráfico para um tipo específico
types = ['fb', 'fp', 'fd', 'rfb', 'rfp', 'rfd', 'rfpb', 'rfpp', 'rfpd', 
         'cfb', 'cfp', 'cfd', 'cfpb', 'cfpp', 'cfpd', 'pa']
type = 'pa'  # Escolha o tipo desejado

plot_fdt_cat(fdt_df, plot_type=type, xlab="Category", ylab="Values", main=f"Type: {type}")
