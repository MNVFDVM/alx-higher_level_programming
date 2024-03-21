#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for h in sorted(my_dict.keys()):
        print("{}: {}".format(h, my_dict[h]))
