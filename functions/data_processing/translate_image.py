import numpy as np
from matplotlib import pyplot as plt


def SSD(I, J):
    """Computing the sum of squared differences (SSD) between two images."""
    if I.shape != J.shape:
        print("Images don't have the same shape.")
        return
    return np.sum((np.array(I, dtype=np.float32) - np.array(J, dtype=np.float32)) ** 2)


def translate_image(I, p, q):
    x_size, y_size = I.shape[:]
    # T = np.array([[1, 0, p], [0, 1, q],[0,0,1]])
    I = np.float32(I)
    I_T = np.zeros(I.shape)
    # Interpolation by rounding p and q
    p = round(p)
    q = round(q)
    I_T[p:, q:] = I[:-p, :-q]
    plt.imshow(I_T)
    plt.show()
