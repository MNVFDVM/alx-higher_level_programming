#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divs = []
    for j in my_list:
        if (j % 2) == 0:
            divs.append(True)
        else:
            divs.append(False)
    return divs
