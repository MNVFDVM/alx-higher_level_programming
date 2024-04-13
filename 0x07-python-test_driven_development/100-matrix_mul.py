#!/usr/bin/python3

"""gtrgt trgtrgtrg trtgtrgtrg tgtrg tgtron."""


def matrix_mul(m_a, m_b):
    """grtgftr rgtrgtrg trgtres.
    Args:
        m_a (list of lists of ints/floats): Thtgtrg rgtrgtrtrix.
        m_b (list of lists of ints/floats): Thefgvfgv fdgfg rgix.
    Raises:
        TypeError: If eifrefref referfref erfertsggrg rtgtrgtrg trg tgtrgts.
        TypeError: Iftgtrgtr trgtrg trgtrgtr trgtrty.
        TypeError: Ifsdffd effre frefref erfrf referows.
        ValueError: jji tgtrgtrg trgtrg fdferf rferfreefed.
    Returns:
        A nedfref reeferf erferf referf refrfre reefreferf erfrefb.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert = []
    for t in range(len(m_b[0])):
        new = []
        for s in range(len(m_b)):
            new.append(m_b[s][t])
        invert.append(new)

    matrix = []
    for row in m_a:
        new = []
        for col in invert:
            prod = 0
            for i in range(len(invert[0])):
                prod += row[i] * col[i]
            new.append(prod)
        matrix.append(new)

    return matrix
