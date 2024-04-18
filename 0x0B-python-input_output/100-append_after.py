#!/usr/bin/python3

"""Definefgrft tcfvfvf frffrr rfrefrffin."""


def append_after(filename="", search_string="", new_string=""):
    """Insfdv ffe gfrefr gfrgr gtrgrg rgtrg trgtrg trgtrg trgile.
    Args:
        filename (str): vgfgvrt gtrg rgtr gle.
        search_string (str): Ttgh trgtr gtrg trgtr gtrgile.
        new_string (str): The sfcfev fdvfvff vfvfvfv fvfrt.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
