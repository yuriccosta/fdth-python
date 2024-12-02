import re

def format_interval(vals, right, pattern):
    # Formats the lower bound
    lower_bound = float(vals[0][1:]) 
    lower_bound_formatted = pattern.format(lower_bound)
    lower_bound_formatted = ("(" if right else "[") + lower_bound_formatted

    # Formats the upper bound
    upper_bound = float(vals[1][:-1])
    upper_bound_formatted = pattern.format(upper_bound)
    upper_bound_formatted = upper_bound_formatted + ("]" if right else ")")

    # Returns the formatted and concatenated boundaries
    return f"{lower_bound_formatted}, {upper_bound_formatted}"

def make_fdt_format_classes(x, right, pattern):
    # Uses regex to separate the x intervals
    tmp = x.apply(str).apply(lambda val: re.findall(r'\([^)]*\)|\[[^\]]*\]', val))
    
    # Applies formatting to each of the ranges
    res = list(map(lambda val: format_interval(val[0].split(','), right, pattern), tmp))

    return res

