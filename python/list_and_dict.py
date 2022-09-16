#!/usr/bin/python3
def min_of_matrix(matrix=[]):
    return min(map(min, matrix))

matrix = [[7, 9, 5, 3], [2, 1, 4, 7], [3, 2, 1, 6]]
print(min_of_matrix(matrix))
