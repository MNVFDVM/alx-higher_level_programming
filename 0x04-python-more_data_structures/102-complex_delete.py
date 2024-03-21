#!/usr/bin/python3
def complex_delete(my_dict, value):
    t = my_dict.copy()
    for h, j in t.items():
        if value == j:
            my_dict.pop(h)
    return my_dict
