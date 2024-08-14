import numpy as np


def matrix_multi_vector1(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_vector2(matrix, vector):
    result = matrix @ vector
    return result
