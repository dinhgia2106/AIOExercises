import numpy as np
from math import sqrt


def compute_vector_length(vector):
    return sqrt(sum(pow(element, 2) for element in vector))


print(np.array([1, 1, 3, 4]))

print(compute_vector_length(np.array([1, 1, 3, 4])))
