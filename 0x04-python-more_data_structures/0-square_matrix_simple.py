#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_list[i][j] = matrix[i][j] ** 2
    return new_list
