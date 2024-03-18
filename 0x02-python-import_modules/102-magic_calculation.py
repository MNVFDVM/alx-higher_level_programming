#!/usr/bin/python3
c_calculation.p

def magic_calclation(x, y):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if x < y:
        s = add(x, y)
        for j in range(4, 6):
            s = add(s, j)
        return (s)

    else:
        return(sub(x, y))
