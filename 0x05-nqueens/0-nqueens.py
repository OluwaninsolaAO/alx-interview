#!/usr/bin/python3
"""Solves the N queens problem"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)


def generate_matrix(N):
    """Generates Matrix of NxN"""
    matrix = []
    for x in range(N):
        for y in range(N):
            matrix.append([x, y])
    return matrix


def resolve_matrix_for(queen, matrix):
    """
    Resolves attack position for queen in matrix then returns
    the position of the next queen not in range of attack.
    """

    def check_visible_cells(queen, matrix):
        def pop_cell(cell):
            """Removes Cell from matrix"""
            matrix.pop(matrix.index(cell))

        matrix_copy = matrix[:]
        for cell in matrix_copy:
            if cell == queen:
                pop_cell(cell)
            elif cell[0] == queen[0]:
                pop_cell(cell)
            elif cell[1] == queen[1]:
                pop_cell(cell)
            elif cell[0] - cell[1] == queen[0] - queen[1]:
                pop_cell(cell)
            elif cell[0] + cell[1] == queen[0] + queen[1]:
                pop_cell(cell)

    check_visible_cells(queen, matrix)

    # checks the best position for the next queen
    if len(matrix) == 0:
        return None
    root_cell = matrix[0]
    root_level_cells = [cell for cell in matrix if
                        cell[0] == root_cell[0]]
    root_collection = {}
    for level_cell in root_level_cells:
        matrix_copy = matrix[:]
        check_visible_cells(level_cell, matrix_copy)
        root_collection.update({tuple(level_cell): len(matrix_copy)})

    sorted_by_len = list(sorted(root_collection.items(),
                                key=lambda item: item[1]))
    print('=>', list(sorted_by_len[-1][0]))
    return list(sorted_by_len[-1][0])


for i in range(N):
    n_queens = []
    matrix = generate_matrix(N)
    queen = [0, i]
    print('\n=>', queen)
    while queen is not None:
        n_queens.append(queen)
        queen = resolve_matrix_for(queen, matrix)

    if len(n_queens) == N:
        print(n_queens)
    # print(n_queens)
