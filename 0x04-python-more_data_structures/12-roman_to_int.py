#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = [d[x] for x in roman_string] + [0]
    r = 0

    for j in range(len(n) - 1):
        if n[j] >= n[j+1]:
            r += n[j]
        else:
            r -= n[j]

    return r
