#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        new_list = []
        for j in range(len(matrix[i])):
            new_list.append(matrix[i][j] * matrix[i][j])
    return new_list
