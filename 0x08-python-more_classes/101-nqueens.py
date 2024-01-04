#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys


def initialize_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return (board)


def deepcopy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(deepcopy_chessboard, chessboard))
    return (chessboard)


def get_queen_positions(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    positions = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == "Q":
                positions.append([row, col])
                break
    return (positions)


def mark_attacked_spots(chessboard, row, col):
    """Mark out spots on a chessboard where non-attacking queens can no longer be placed."""
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(chessboard):
        solutions.append(get_queen_positions(chessboard))
        return (solutions)

    for col in range(len(chessboard)):
        if chessboard[row][col] == " ":
            temp_board = deepcopy_chessboard(chessboard)
            temp_board[row][col] = "Q"
            mark_attacked_spots(temp_board, row, col)
            solutions = recursive_solve(temp_board, row + 1, queens + 1, solutions)

    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)
