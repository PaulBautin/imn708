# -*- coding: utf-8 -*-
import logging
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RangeSlider, Button
import numpy as np

from functions.data_processing.compute_mip import mip_img, MIP_img



def viewer_comparaison(img_original, img_transformed):
    """
    Inspired by https://matplotlib.org/stable/gallery/widgets/slider_demo.html
    method: str
        Should be either 'method1' or 'method2'
    """
    # find middle axial slice
    img_shape = img_original.shape
    middle_axial_slice = int(img_shape[2] // 2)
    # plot img comparaison
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(img_original[:, :, middle_axial_slice].T, origin='lower')
    ax[0].set_title("Original image")
    ax[1].imshow(img_transformed[:, :, middle_axial_slice].T, origin='lower')
    ax[1].set_title("Transformed image")
    plt.show()


