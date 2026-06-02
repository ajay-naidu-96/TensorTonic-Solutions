import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x *= -1
    print(x)
    return (1.0/(1+np.exp(x)))