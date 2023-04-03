#!/usr/bin/python3
"""
The ``2-matrix_divided`` module divides all elements of a matrix
by a given number.
This module supplies a function named ``matrix_divided()``

Example:

>>>matrix_divided(matrix = [[1,2,3], [5,6,7]], div)
[1,2,3], [4,5,6]
"""
add = __import__("0-add_integer").add_integer


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix and returns the new matrix """
    li = all(isinstance(i, list) for i in matrix)
    if not li:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    for row in matrix:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix " +
                                " (list of lists) of integers/floats")
    row_len = [len(row) for row in matrix]
    r_size = set(row_len)
    if (len(r_size)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrx = [[round(col / div, 2) for col in row] for row in matrix]
    return (new_matrx)


if __name__ == "__main__":
    matrix_divided([[1, 7, 8.9], [8, 6, 9]], 9)
