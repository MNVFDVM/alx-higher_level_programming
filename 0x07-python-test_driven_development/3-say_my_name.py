#!/usr/bin/python3

"""Defindfgvfd dffdgfdgdf fdgfdgfdn."""

def say_my_name(first_name, last_name=""):
    """Prigrg rgregtre.
    Args:
        first_name (str): The gftrg fdgfdgint.
        last_name (str): Thefgrfg dfgfdgfg print.
    Raises:
        TypeError: If eithdfd fdgdfgfdgfd fdgrings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
