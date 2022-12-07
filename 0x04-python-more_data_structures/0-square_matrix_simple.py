#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nbr_raw = len(matrix)
    new_matrix = [[x for x in range(len(matrix[0]))] for y in range(nbr_raw)]
    for i in range(nbr_raw):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j]**2
    return new_matrix
