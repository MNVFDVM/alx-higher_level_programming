#!/usr/bin/python3

"""Defines a class-checking functi"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class)
