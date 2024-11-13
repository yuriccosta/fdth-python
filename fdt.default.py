import numpy as np
import pandas as pd

def calculate_sturges(x):
    return int(np.ceil(1 + 3.322 * np.log10(len(x))))

def calculate_scott(x):
    std_dev = np.std(x)
    return int(np.ceil((x.max() - x.min()) / (3.5 * std_dev / (len(x) ** (1 / 3)))))

def calculate_fd(x):
    iqr = np.percentile(x, 75) - np.percentile(x, 25)
    return int(np.ceil((x.max() - x.min()) / (2 * iqr / (len(x) ** (1 / 3)))))

def make_fdt_simple(x, start, end, h, right=False):
    bins = np.arange(start, end + h, h)
    labels = [f"{round(bins[i], 2)} - {round(bins[i + 1], 2)}" for i in range(len(bins) - 1)]
    f = pd.cut(x, bins=bins, right=right, labels=labels).value_counts()
    rf = f / len(x)
    rfp = rf * 100
    cf = f.cumsum()
    cfp = (cf / len(x)) * 100
    
    table = pd.DataFrame({
        'Class limits': labels,
        'f': f.values,
        'rf': rf.values,
        'rf(%)': rfp.values,
        'cf': cf.values,
        'cf(%)': cfp.values
    })
    
    return table

def fdt_default(x, k=None, start=None, end=None, h=None, breaks='Sturges', right=False, na_rm=False):
    x = np.array(x)
    if na_rm:
        x = x[~np.isnan(x)]
    elif np.any(np.isnan(x)):
        raise ValueError("O vetor contém valores NA e 'na_rm' é definido como False.")
    
    if k is None and start is None and end is None and h is None:
        if breaks == 'Sturges':
            k = calculate_sturges(x)
        elif breaks == 'Scott':
            k = calculate_scott(x)
        elif breaks == 'FD':
            k = calculate_fd(x)
        else:
            raise ValueError("Método de 'breaks' inválido.")
        start, end = x.min() - abs(x.min()) / 100, x.max() + abs(x.max()) / 100
        R = end - start
        h = R / k
    elif start is None and end is None and h is None:
        start, end = x.min() - abs(x.min()) / 100, x.max() + abs(x.max()) / 100
        R = end - start
        h = R / k
    elif k is None and h is None:
        R = end - start
        k = int(np.sqrt(abs(R)))
        k = max(k, 5)
        h = R / k
    elif k is None:
        pass
    else:
        raise ValueError("Parâmetros fornecidos são incompatíveis. Verifique a função.")
    
    table = make_fdt_simple(x, start, end, h, right)
    breaks_info = {'start': start, 'end': end, 'h': h, 'right': int(right)}
    result = {'table': table, 'breaks': breaks_info}
    
    return result
#Testes
""" 
dados = np.array([1.1, 2.2, 3.3, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
resultado = fdt_default(dados, breaks='Sturges')
print(resultado['table'])
print("Parâmetros:", resultado['breaks'])

dados = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])
resultado = fdt_default(dados, breaks='Scott')
print(resultado['table'])
print("Parâmetros:", resultado['breaks'])

dados = np.array([1, 1.5, 2, 2.5, 3, 4.5, 5.5, 7, 8, 8.5, 9, 10, 11, 12, 14, 15])
resultado = fdt_default(dados, breaks='FD')
print(resultado['table'])
print("Parâmetros:", resultado['breaks'])
"""
dados = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
resultado = fdt_default(dados, breaks='Sturges')
print(resultado['table'])
print("Parâmetros:", resultado['breaks'])
