import re

def format_interval(vals, right, pattern):
    # if len(vals) != 2:
    #     raise ValueError("Each interval must have two values.")

    # Faz a formatação do limite inferior
    lower_bound = float(vals[0][1:]) 
    lower_bound_formatted = pattern.format(lower_bound)
    lower_bound_formatted = ("(" if right else "[") + lower_bound_formatted

    # Faz a formatação do limite superior
    upper_bound = float(vals[1][:-1])
    upper_bound_formatted = pattern.format(upper_bound)
    upper_bound_formatted = upper_bound_formatted + ("]" if right else ")")

    # Retorna os limites formatados e concatenados
    return f"{lower_bound_formatted}, {upper_bound_formatted}"

def make_fdt_format_classes(x, right, pattern):
    # Usa regex para separar os intervalos de x 
    tmp = x.apply(str).apply(lambda val: re.findall(r'\([^)]*\)|\[[^\]]*\]', val))
    
    # Aplica a formatação a cada um dos intervalos
    res = list(map(lambda val: format_interval(val[0].split(','), right, pattern), tmp))

    return res

