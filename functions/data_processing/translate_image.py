import numpy as np
from matplotlib import pyplot as plt


def translate_image(I, p, q):
    # x_size, y_size = I.shape[:]
    # T = np.array([[1, 0, p], [0, 1, q],[0,0,1]])
    I = np.float32(I)
    I_T = np.zeros(I.shape)
    # Interpolation by rounding p and q
    p = round(p)
    q = round(q)
    I_T[q:, p:] = I[:-q, :-p]
    # plt.imshow(I_T)
    # plt.show()

    return I_T
