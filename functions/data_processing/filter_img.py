# -*- coding: utf-8 -*-
import logging

from scipy import ndimage
from scipy.ndimage import gaussian_filter, median_filter
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np
from functions.img_viewer.img_comparaison import viewer_comparaison


def denoise_img(img, method):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # Prepare image for the denoising
    # img += parameter1
    # img += parameter2
    img_data = np.asarray(img.get_fdata())

    # Actually do the denoising
    if method == 'nl_means':
        logging.debug("Using nl means filter!")
        img_denoised = nl_means_filter(img_data)
        viewer_comparaison(img_data, img_denoised)
    elif method == 'gaussian':
        logging.debug("Using gaussian filter!")
        img_denoised = median_filter(img_data)
        viewer_comparaison(img_data, img_denoised)
    elif method == 'median':
        logging.debug("Using median filter!")
        img_denoised = gaussian_filter(img_data)
        viewer_comparaison(img_data, img_denoised)
    else:
        raise ValueError("Chosen method not understood.")

    return img_denoised


def nl_means_filter(img, fast=None):
    """
    blabla
    use_method_y: bool
        If true, use method y. Else, use method x.
    """
    # estimate the noise standard deviation from the noisy image
    sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))
    print(f'estimated noise standard deviation = {sigma_est}')

    patch_kw = dict(patch_size=7,  # 7x7x7 patches
                    patch_distance=11,  # 23x23x23 search area
                    channel_axis=-1)
    if fast:
        logging.debug("Using fast method!")
        # fast algorithm
        img_denoised = denoise_nl_means(img, h=0.6 * sigma_est, fast_mode=True, **patch_kw)
    else:
        logging.debug("NOT using fast method!")
        # slow algorithm
        img_denoised = denoise_nl_means(img, h=1 * sigma_est, fast_mode=False, **patch_kw)
    return img_denoised


def median_filter(img):
    """
        blabla
        use_method_y: bool
            If true, use method y. Else, use method x.
        """
    logging.debug("Using method Y!")
    img_denoised = ndimage.median_filter(img, size=5)
    return img_denoised

def gaussian_filter(img, gradient_magnitude=None):
    """
    Method of linear filtering
    use_method_y: bool
            If true, use method y. Else, use method x.
        """
    if gradient_magnitude:
        logging.debug("Using gaussian filter!")
        img_denoised = gaussian_filter(img, sigma=2)
    else:
        logging.debug("Using gradient magnitude!")
        img_denoised = ndimage.gaussian_gradient_magnitude(img, sigma=2)
    return img_denoised


















