#!/usr/bin/python3

"""Definefgfg fddgdfgfdg dfgfdgfon."""


def text_indentation(text):
    """Prigf grfgrtg rgtrgrtgtr trgtrgtrg rfgtrgtrg trgtrgtr.
    Args:
        text (string): dfvdfvrf refrefreft.
    Raises:
        TypeError: Iffgrfg fgrgtrg trgtg.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = 0
    while s < len(text) and text[s] == ' ':
        s += 1

    while s < len(text):
        print(text[s], end="")
        if text[s] == "\n" or text[s] in ".?:":
            if text[s] in ".?:":
                print("\n")
            s += 1
            while s < len(text) and text[s] == ' ':
                s += 1
            continue
        s += 1
