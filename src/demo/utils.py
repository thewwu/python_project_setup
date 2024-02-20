import numpy as np


def mean(x: list):
    return np.mean(x)


def median(x: list):
    return np.median(x)


def run():
    x = [1,2,4]
    print(f"Mean   of {x}: {mean(x):.2f}")
    print(f"Median of {x}: {median(x):.2f}")
    
    return
    