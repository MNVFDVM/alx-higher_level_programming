#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for j in my_string:
        if (j != 'c') and (j != 'C'):
            new_str += j
    return (new_str)
