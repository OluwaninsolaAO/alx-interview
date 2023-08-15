#!/usr/bin/python3
"""0. Rotate 2D Matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees Clockwise"""
    n = len(matrix)
    copy = matrix[:]
    for y in range(n):
        x = n - 1
        dx = []
        while x >= 0:
            dx.append(matrix[x][y])
            x -= 1
        matrix.append(dx)
    for dx in copy:
        matrix.pop(matrix.index(dx))
