import numpy as np


def matrix_multi_matrix1(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


def matrix_multi_matrix2(matrix1, matrix2):
    result = matrix1 @ matrix2
    return result
