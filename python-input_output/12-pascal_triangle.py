#!/usr/bin/python3
"""Defines the pascal triangle that returns a list of lists of integers."""


def pascal_triangle(n):
    """return a list of lists of integers of pascal triangle

    Args:
        n (int): The number of rows
    Returns:
        The nth row of Pascal's triangle
    """

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
