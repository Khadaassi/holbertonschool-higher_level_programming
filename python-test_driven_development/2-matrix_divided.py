#!/usr/bin/python3

"""

This module defines a matrix division function.

"""


def matrix_divided(matrix, div):
    """
    Divide all elts of a matrix by a number

    Args:
        matrix (list of lists): matrix to be divided
        div (int or float): number to divide the matrix by
    Raises:
        TypeError: if matrix is not a list or is empty
        TypeError: if matrix contains non int or float elts
        TypeError: if rows of matrix are of differents sizes
        TypesError: if div is not an int or a float
        ZeroDivisionError: if div is 0
    Return:
        new_matrix (list of lists):a new matrix w/ elts divided by div
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (
        not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)
    ):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
