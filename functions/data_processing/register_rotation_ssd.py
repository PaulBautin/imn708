import numpy as np

from functions.data_processing.register_translation_ssd import SSD
from functions.data_processing.rotate_image import rotate_image
from matplotlib import pyplot as plt


def register_rotation_ssd(I,J):
    I = np.float32(I)
    J = np.float32(J)
    theta = -180
    ssd = [float('inf')]
    rotation = []
    while theta < 180:
        I_R = rotate_image(I, theta)
        ssd.append(SSD(I_R, J))
        if ssd[-1] < ssd[-2]:
            theta = theta + .6
        else:
            theta = theta + .3
        rotation.append(theta)
    print(rotation[ssd.index(min(ssd))])
    # print(ssd_y)
    plt.plot(rotation, ssd[1:])
    plt.show()
