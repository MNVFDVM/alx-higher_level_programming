#!/usr/bin/python3

"""Defindfgf dfgfdgfdg fdgfdgn."""

def print_square(size):
    """Printrgtr rfgrfgtrg rgtrgacter.
    Args:
        size (int): Thedffe erferfref erfruare.
    Raises:
        TypeError: Ifrgtr fgrfgtr rgreger.
        ValueError: fder dfrere ref0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
