#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_list.append(matrix[i][j] * matrix[i][j])
    return new_list
