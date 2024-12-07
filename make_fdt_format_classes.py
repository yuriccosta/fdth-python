import pandas as pd
import re

def format_interval(vals, right, pattern):
    # Checks for two valid elements in the range
    if len(vals) != 2:
        raise ValueError(f"Invalid range: {vals}")

    # Formats the lower bound
    lower_bound = float(vals[0].strip('[').strip('('))  # removes the '[' or '('
    lower_bound_formatted = pattern.format(lower_bound)
    lower_bound_formatted = ("(" if right else "[") + lower_bound_formatted

    # Formats the upper bound
    upper_bound = float(vals[1].strip(']').strip(')'))  # removes the ']' or ')'
    upper_bound_formatted = pattern.format(upper_bound)
    upper_bound_formatted = upper_bound_formatted + ("]" if right else ")")

    # Returns the formatted and concatenated boundaries
    return f"{lower_bound_formatted}, {upper_bound_formatted}"

def make_fdt_format_classes(x, right, pattern):
    # Ensures that the intervals are in the correct format
    def parse_interval(val):
        # Uses regex to identify ranges in the format [a, b) or (a, b]
        match = re.match(r"[\[\(]\d+(\.\d+)?\s*,\s*\d+(\.\d+)?[\]\)]", val)
        if match:
            return match.group(0).split(',')
        else:
            raise ValueError(f"Invalid range: {val}")

    # Applies the range checking and formatting
    tmp = x.apply(lambda val: parse_interval(val))
    
    # Format the intervals
    res = tmp.apply(lambda val: format_interval(val, right, pattern))

    return res
