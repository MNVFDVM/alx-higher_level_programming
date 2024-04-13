#!/usr/bin/python3

"""Def DSFDSFDSF fddgdgfd nction."""


def matrix_divided(matrix, div):
    """Divrgdf fdgfdgfdgfdgfd dsfdsfds.
    Args:
        matrix (list): A dgffd rfrefrefref floats.
        div (int/float): Thdfgfdgor.
    Raises:
        TypeError: Igtrgtr gfrg ergregreg mbers.
        TypeError: Iffvf dffgfdgffdgfdfd izes.
        TypeError: Ifrefrefre fr refrefreferf.
        ZeroDivisionError: Ireffdg ffeffger0.
    Returns:
        A new mfgfeg dfgregrgtrg gfegergsion.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
