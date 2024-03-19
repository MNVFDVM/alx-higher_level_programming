#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = my_list[:]
    for c, i in enumerate(my_list):
        if i % 2 == 0:
            b[c] = True
        else:
            b[c] = False
    return(b)
