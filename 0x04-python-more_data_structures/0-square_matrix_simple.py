#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for rows in matrix:
        return(list(map(lambda x:x ** 2, rows)))
