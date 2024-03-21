#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    d = 0

    for p in my_list:
        n += p[0] * p[1]
        d += p[1]

    return (n / d)
