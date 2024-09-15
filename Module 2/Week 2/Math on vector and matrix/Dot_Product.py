import numpy as np


def compute_dot_prodct(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")

    result = sum(v * u for v, u in zip(vector1, vector2))
    return result


vector1 = np.array([1, 3, 5, 6])
vector2 = np.array([4, 2, 7, 2])

print(compute_dot_prodct(vector1, vector2))
