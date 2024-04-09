#!/usr/bin/python3

import sys

def init_board(n):
    b = []
    [b.append([]) for k in range(n)]
    [row.append(' ') for k in range(n) for row in b]
    return (b)

def board_deepcopy(board):
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)

def get_solution(board):
    s = []
    for y in range(len(board)):
        for v in range(len(board)):
            if board[y][v] == "Q":
                solution.append([y, v])
                break
    return (s)

def xout(board, row, col):
    for v in range(col + 1, len(board)):
        board[row][v] = "x"
    for v in range(col - 1, -1, -1):
        board[row][v] = "x"
    for y in range(row + 1, len(board)):
        board[y][col] = "x"
    for y in range(row - 1, -1, -1):
        board[y][col] = "x"
    v = col + 1
    for y in range(row + 1, len(board)):
        if v >= len(board):
            break
        board[y][v] = "x"
        v += 1
    v = col - 1
    for y in range(row - 1, -1, -1):
        if v < 0:
            break
        board[y][v]
        v -= 1
    v = col + 1
    for y in range(row - 1, -1, -1):
        if v >= len(board):
            break
        board[y][v] = "x"
        v += 1
    v = col - 1
    for y in range(row + 1, len(board)):
        if v < 0:
            break
        board[y][v] = "x"
        v -= 1

def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for v in range(len(board)):
        if board[row][v] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][v] = "Q"
            xout(tmp_board, row, v)
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
    for l in solutions:
        print(l)
