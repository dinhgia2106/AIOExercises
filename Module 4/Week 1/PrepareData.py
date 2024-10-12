import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

def get_column(data, index):
    result = [row[index] for row in data]
    return result

def prepare_data(file_name_dataset):
    data = np.genfromtxt(file_name_dataset, delimiter=',', skip_header=1).tolist()
    N = len(data)

    tv_data = get_column(data, 0)
    
    radio_data = get_column(data, 1)

    newspaper_data = get_column(data, 2)

    sales_data = get_column(data, 3)

    X = [tv_data, radio_data, newspaper_data]
    Y = sales_data

    return X, Y

