def format_interval(vals, right, pattern):
    # Formata o limite inferior
    lower_bound = float(vals[0].strip())  # Converte o limite inferior para float
    lower_bound_formatted = pattern.format(lower_bound)
    lower_bound_formatted = ("(" if right else "[") + lower_bound_formatted

    # Formata o limite superior
    upper_bound = float(vals[1].strip())  # Converte o limite superior para float
    upper_bound_formatted = pattern.format(upper_bound)
    upper_bound_formatted = upper_bound_formatted + ("]" if right else ")")

    # Retorna os limites formatados e concatenados
    return f"{lower_bound_formatted}, {upper_bound_formatted}"

def make_fdt_format_classes(x, right, pattern):
    # Converte a string "2.84 - 3.76" em intervalos no formato [2.84, 3.76]
    res = x.apply(lambda val: format_interval(val.split(' - '), right, pattern))
    
    return res
