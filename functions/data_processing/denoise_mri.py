# -*- coding: utf-8 -*-
import logging


def denoise_img(img, parameter1, parameter2, method):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # Prepare image for the denoising
    img += parameter1
    img += parameter2

    # Actually do the denoising
    if method == 'method1':
        logging.debug("Using method1!")
        img_denoised = img
    elif method == 'method2':
        raise NotImplementedError  # Not ready yet!
    else:
        raise ValueError("Chosen method not understood.")

    return img_denoised


def use_img_to_create_something(img, use_method_y):
    """
    blabla
    use_method_y: bool
        If true, use method y. Else, use method x.
    """
    if use_method_y:
        logging.debug("Using method Y!")
        result = 1
    else:
        logging.debug("NOT using method Y!")
        result = 5

    return result
