import numpy as np
from matplotlib import pyplot as plt
from skimage import io


def rotate_image(I, theta):

    I_R = np.zeros(I.shape, dtype=np.uint32)

    T = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])

    for i, row in enumerate(I):
        for j, col in enumerate(row):
            pixel_data = I[i, j]  # get the value of pixel at corresponding location
            input_coord = np.array([i, j])  # this will be my [x,y] matrix
            result = T @ input_coord
            i_r, j_r = result  # store the resulting coordinate location

            # make sure the i and j values remain within the index range
            if (0 < int(i_r) < I.shape[0]) and (0 < int(j_r) < I.shape[1]):
                I_R[int(i_r)][int(j_r)] = pixel_data

    # plt.imshow(I_R)
    # plt.show()
    return I_R
