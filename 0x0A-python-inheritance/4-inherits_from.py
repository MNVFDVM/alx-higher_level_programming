#!/usr/bin/python3

"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checksfgerf referf erfr ferf erfreerfer ferferfss.
    Args:
        obj : The obfdverf efrefre ck.
        a_class (type): The clfre erferf erferref erfo.
    Returns:
        If ofer ferfrefer frfer f refress - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
