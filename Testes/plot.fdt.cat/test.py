import pandas as pd
from plot_fdt_cat_default import plot_fdt_cat

# Test data
data = {
    'Category': ["Security", "Traffic", "Public Transport", "Health", "Education", "Others"],
    'Frequency': [18, 17, 16, 7, 5, 3],
    'Relative Frequency': [0.27, 0.26, 0.24, 0.11, 0.08, 0.05],
    'Relative Frequency %': [27, 26, 24, 11, 8, 5],
    'Cumulative Frequency': [18, 35, 51, 58, 63, 66],
    'Cumulative Frequency %': [27, 53, 77, 88, 95, 100]
}

df = pd.DataFrame(data)

# Plot types for testing
types = ['fb', 'fp', 'fd', 'rfb', 'rfp', 'rfd', 'rfpb', 'rfpp', 'rfpd', 
         'cfb', 'cfp', 'cfd', 'cfpb', 'cfpp', 'cfpd', 'pa']

type = types[0]

plot_fdt_cat(df, plot_type=type, xlab="Category", ylab="Values", main=f"Type: {type}")