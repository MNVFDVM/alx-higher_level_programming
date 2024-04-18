#!/usr/bin/python3

"""Defregttr rgfregfr egtrgr grgrgr grg rgrgr rgrcts."""


def add_attribute(obj, att, value):
    """Addferf erferf refer fer freferfer ferfrefer fble.
    Args:
        obj (any): Thferf frefre frefer frefer fceo.
        att (str): The rgr eferf erferf erferferobj.
        value (any): The vfer edfreftt.
    Raises:
        TypeError: Iferfre erfref erfrefer frefded.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
