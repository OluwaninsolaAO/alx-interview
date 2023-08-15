#!/usr/bin/python3
"""0. Rotate 2D Matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees Clockwise"""
    n = len(matrix)
    copy = matrix[:]
    for y in range(n):
        dx = []
        for x in range(n-1, -1, -1):
            dx.append(matrix[x][y])
        matrix.append(dx)
    for dx in copy:
        matrix.pop(matrix.index(dx))
