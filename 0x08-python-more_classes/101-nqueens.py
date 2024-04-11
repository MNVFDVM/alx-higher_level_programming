#!/usr/bin/python3
"""Solvetfgh gtrg grtuzzle.

Detetrgtrg tgtrg gtg  placing 
N fdfdgfdgdfgfd  gtrtrc hessboard.

Example:
    $ ./101-nqueens.py N

N mhfhbhgfhgfto 4.

Attributes:
    board (list): A lisfhbgfhbfhessboard.
    solutions (list): A listbgfbgfbgutions.

Soludfvfdv  jcxjnc udscu jdcu dsuicdsi  iic ci sdic8i dcf
wheregfhgfhbgfjbdfov djodnvodivd odvoidjvfd vooovdfov odfvod
quhessboard.
"""
import sys


def init_board(n):
    """Initializhtyoard withs."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Returghgssboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Returgfhgfhghhessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """fgdfbgfbfssboard.

    All fbvfbgfn no
    longbgfbgfhbgout.

    Args:
        board (list): The currefdgfsboard.
        row (int): The rfvfcgblayed.
        col (int): The columgfhplayed.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursxcvbczzle.

    Args:
        board (list): The cufdgfdsboard.
        row (int): The cufgvdfgow.
        queens (int): The currelaced quyghens.
        solutions (list): A lisions.
    Returns:
        solutirfref
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
