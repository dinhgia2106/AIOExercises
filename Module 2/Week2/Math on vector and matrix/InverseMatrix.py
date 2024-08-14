import numpy as np


def inverse_matrix(matrix):
    det = np.linalg.det(matrix)

    if det != 0:
        result = np.linalg.inv(matrix)
    else:
        result = None

    return result
