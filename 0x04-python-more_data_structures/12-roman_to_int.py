#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if not isinstance(roman_string, str):
        return 0
    t = 0
    n = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'c': 100, 'D': 500, 'M': 1000}
    for f in reversed(roman_string):
        n = d[f]
        t += n if t < n * 5 else -n
    return t
