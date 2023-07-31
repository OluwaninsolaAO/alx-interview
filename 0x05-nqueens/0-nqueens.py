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


def resolve_matrix_for(queen, matrix, positions):
    """
    Resolves attack position for queen in matrix then recursively
    resolves for subsequent possible level positions.
    """
    positions.append(queen)

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

    # if end of the line
    if len(matrix) == 0:
        if len(positions) == N:
            print(positions)
        return

    for possible_queen in [cell for cell in matrix if
                           cell[0] == matrix[0][0]]:
        resolve_matrix_for(possible_queen, matrix[:], positions[:])


for i in range(N):
    resolve_matrix_for([0, i], generate_matrix(N), [])
